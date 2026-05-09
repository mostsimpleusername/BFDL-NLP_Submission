import pandas as pd
from google_play_scraper import reviews, Sort
from tqdm import tqdm
import time

# List aplikasi sekuritas (Play Store ID)
apps = {
    "Ajaib": "ajaib.co.id",
    "Bibit": "com.bibit.bibitid",
    "Stockbit": "com.stockbit.android",
    "IPOT": "com.indopremier.ipot"
}

all_reviews = []

# Target per app (biar total >10k)
TARGET_PER_APP = 4000

for app_name, app_id in apps.items():
    print(f"\nScraping {app_name}...")

    count = 0
    continuation_token = None

    while count < TARGET_PER_APP:
        result, continuation_token = reviews(
            app_id,
            lang='id',
            country='id',
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )

        for r in result:
            # Menambahkan semua key dari r ke dalam list, ditambah nama aplikasi
            review_data = r.copy()
            review_data['app'] = app_name
            all_reviews.append(review_data)

        count += len(result)
        print(f"{app_name}: {count} reviews collected")

        # Safety delay
        time.sleep(1)

        if not continuation_token:
            break

# Convert ke DataFrame
df = pd.DataFrame(all_reviews)

print("\nScraping selesai!")
print(f"Total data: {len(df)}")
print("Columns available:", df.columns.tolist())

# Memastikan kolom 'app' ada di depan untuk kemudahan visual
cols = ['app'] + [c for c in df.columns if c != 'app']
df = df[cols]

# Simpan
df.to_csv("reviews_sekuritas.csv", index=False)