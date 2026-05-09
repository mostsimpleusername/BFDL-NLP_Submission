import logging
import os
import random
import time

import pandas as pd
from google_play_scraper import Sort, reviews


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TARGET_APPS = [
    {"app_id": "com.bibit.id", "app_name": "bibit"},
    {"app_id": "id.ajaib.app", "app_name": "ajaib"},
    {"app_id": "com.stockbit.android", "app_name": "stockbit"},
    {"app_id": "id.co.indopremier.ipotstock", "app_name": "ipot"},
]

RETAINED_COLUMNS = [
    "app",
    "reviewId",
    "content",
    "score",
    "at",
    "thumbsUpCount",
]


def _safe_sleep():
    delay = random.uniform(1.0, 3.0)
    logging.info("Sleeping for %.2f seconds to avoid rate limiting.", delay)
    time.sleep(delay)


def _fetch_reviews(app_id, sort_order, count):
    logging.info("Fetching %s reviews with sort=%s", app_id, sort_order.name)
    batch_size = min(200, count)
    collected_reviews = []
    continuation_token = None

    while len(collected_reviews) < count:
        remaining = count - len(collected_reviews)
        current_batch_size = min(batch_size, remaining)
        result, continuation_token = reviews(
            app_id,
            lang="id",
            country="id",
            sort=sort_order,
            count=current_batch_size,
            continuation_token=continuation_token,
        )

        if not result:
            logging.info("No additional reviews returned for %s using %s.", app_id, sort_order.name)
            break

        collected_reviews.extend(result)
        logging.info(
            "Collected %d/%d reviews for %s using %s.",
            len(collected_reviews),
            count,
            app_id,
            sort_order.name,
        )
        _safe_sleep()

        if continuation_token is None:
            break

    return collected_reviews


def scrape_app(app_id, app_name, count=5000):
    logging.info("Starting scrape for %s (%s)", app_name, app_id)
    collected_frames = []

    for sort_order in (Sort.NEWEST, Sort.MOST_RELEVANT):
        try:
            records = _fetch_reviews(app_id=app_id, sort_order=sort_order, count=count)
            batch_df = pd.DataFrame(records)
            if batch_df.empty:
                logging.info("No reviews returned for %s using %s.", app_name, sort_order.name)
                continue

            batch_df["app"] = app_name
            collected_frames.append(batch_df)
            logging.info(
                "Collected %d rows for %s using %s.",
                len(batch_df),
                app_name,
                sort_order.name,
            )
        except Exception as exc:
            logging.exception(
                "Failed to scrape %s (%s) with %s: %s",
                app_name,
                app_id,
                sort_order.name,
                exc,
            )

    if not collected_frames:
        logging.warning("No reviews collected for %s.", app_name)
        return pd.DataFrame(columns=RETAINED_COLUMNS)

    app_df = pd.concat(collected_frames, ignore_index=True)
    app_df = app_df.drop_duplicates(subset=["reviewId"])

    missing_columns = [
        column
        for column in [
            "app",
            "reviewId",
            "userName",
            "content",
            "score",
            "at",
            "thumbsUpCount",
            "replyContent",
            "repliedAt",
        ]
        if column not in app_df.columns
    ]
    if missing_columns:
        logging.warning("Missing columns for %s: %s", app_name, missing_columns)
        for column in missing_columns:
            app_df[column] = None

    app_df = app_df[
        [
            "app",
            "reviewId",
            "userName",
            "content",
            "score",
            "at",
            "thumbsUpCount",
            "replyContent",
            "repliedAt",
        ]
    ]
    app_df = app_df.drop(columns=["userName", "replyContent", "repliedAt"], errors="ignore")
    app_df = app_df[RETAINED_COLUMNS]

    logging.info("Finished %s with %d deduplicated reviews.", app_name, len(app_df))
    return app_df


if __name__ == "__main__":
    random.seed(42)
    all_frames = []

    for app_config in TARGET_APPS:
        app_df = scrape_app(
            app_id=app_config["app_id"],
            app_name=app_config["app_name"],
            count=5000,
        )
        all_frames.append(app_df)

    if all_frames:
        merged_df = pd.concat(all_frames, ignore_index=True)
    else:
        merged_df = pd.DataFrame(columns=RETAINED_COLUMNS)

    merged_df = merged_df.drop_duplicates(subset=["reviewId"])
    merged_df["content"] = merged_df["content"].fillna("").astype(str)
    merged_df = merged_df[merged_df["content"].str.strip() != ""].reset_index(drop=True)

    output_dir = "data"
    output_path = os.path.join(output_dir, "dataset_raw.csv")
    os.makedirs(output_dir, exist_ok=True)

    try:
        merged_df.to_csv(output_path, index=False)
        logging.info("Saved merged dataset to %s", output_path)
    except Exception as exc:
        logging.exception("Failed to save dataset to %s: %s", output_path, exc)
        raise

    print(f"Final row count: {len(merged_df)}")
    print("Per-app review counts:")
    print(merged_df["app"].value_counts())
