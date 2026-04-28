# 📊 Indonesian Financial App Sentiment Analysis

### NLP Project · Google Play Store Reviews · 3-Class Classification

---

## 🚀 Overview

This project builds an **end-to-end sentiment analysis pipeline** for Indonesian-language user reviews from major financial (sekuritas) mobile applications on the Google Play Store.

The system automatically classifies reviews into:

* **Negative**
* **Neutral**
* **Positive**

Target applications:

* Bibit
* Ajaib
* Stockbit
* IPOT

The project is designed as:

* 🎓 Academic NLP submission
* 💼 Portfolio-ready AI engineering project
* ⚙️ Reproducible ML pipeline

---

## 🎯 Objectives

* Scrape and build a dataset of **≥10,000 reviews**
* Perform **3-class sentiment classification**
* Train **≥3 machine learning models**
* Achieve **≥85% test accuracy**
* Provide **inference on unseen text**
* Deliver a **fully reproducible pipeline**

---

## 📂 Project Structure

```
├── data/
│   ├── dataset_raw.csv
│   └── dataset_processed.csv
│
├── notebooks/
│   └── sentiment_analysis_sekuritas.ipynb
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   ├── model_lr.pkl
│   ├── model_svm.pkl
│   └── model_rf.pkl
│
├── src/
│   ├── scraper.py
│   ├── preprocessing.py
│   └── slang_dict.py
│
├── word2vec.model
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* **Source:** Google Play Store (public reviews)
* **Language:** Indonesian (mixed informal + slang)
* **Size:** ≥10,000 reviews
* **Apps Covered:** Bibit, Ajaib, Stockbit, IPOT

### Data Schema

| Column        | Description        |
| ------------- | ------------------ |
| app           | Source application |
| reviewId      | Unique review ID   |
| content       | Raw review text    |
| score         | Rating (1–5)       |
| at            | Timestamp          |
| thumbsUpCount | Helpfulness votes  |
| sentiment     | Label (derived)    |

---

## 🏷️ Labeling Strategy

Labels are generated using rating-based rules:

| Score | Sentiment |
| ----- | --------- |
| 1–2   | Negative  |
| 3     | Neutral   |
| 4–5   | Positive  |

> ⚠️ Note: This introduces some noise but is a standard scalable approach.

---

## 🧹 Preprocessing Pipeline

The pipeline is designed specifically for **informal Indonesian text**.

### Steps:

* Lowercasing
* URL & symbol removal
* Slang normalization (e.g., *"gak" → "tidak"*)
* Stopword removal (**negation preserved**)
* Tokenization

### ⚠️ Important Design Decision:

Negation words like:

```
tidak, bukan, kurang
```

are **NOT removed**, because they invert sentiment.

---

## 🧠 Feature Engineering

### 1. TF-IDF

* Unigrams + Bigrams
* Max features: 10,000
* Sparse representation

### 2. Word2Vec

* Vector size: 100
* Trained on dataset
* Document vector = average word embeddings

---

## 🤖 Models & Experiments

| Experiment | Features | Model               |
| ---------- | -------- | ------------------- |
| EXP-01     | TF-IDF   | Logistic Regression |
| EXP-02     | TF-IDF   | SVM                 |
| EXP-03     | Word2Vec | Random Forest       |

### Tuning:

* GridSearchCV
* 5-fold cross-validation
* Metric: **Macro F1-score**

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* **Macro F1-score (primary)**
* Confusion Matrix

> Macro F1 is used to handle **class imbalance**.

---

## 🧪 Results (Example)

| Model               | Accuracy | Macro F1 |
| ------------------- | -------- | -------- |
| Logistic Regression | 0.87     | 0.85     |
| SVM                 | 0.89     | 0.87     |
| Random Forest       | 0.83     | 0.80     |

> ✅ Best model exceeds **85% accuracy requirement**

---

## 🔍 Insight Extraction

Beyond classification, the project extracts:

* Most common **positive keywords**
* Most frequent **complaints**
* Sentiment distribution per app
* Example reviews per class

This simulates real-world usage for:

* Product teams
* Market analysis

---

## 🧪 Inference Example

```python
predict_sentiment("aplikasinya gak bisa login, error terus")
# Output: "negative"
```

### Sample Inputs:

| Input                          | Prediction |
| ------------------------------ | ---------- |
| "aplikasinya bagus banget"     | Positive   |
| "tidak bisa login sama sekali" | Negative   |
| "lumayan tapi masih ada bug"   | Neutral    |

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Run scraping script:

```bash
python src/scraper.py
```

2. Open notebook:

```bash
jupyter notebook notebooks/sentiment_analysis_sekuritas.ipynb
```

3. Run all cells from top to bottom

---

## 📦 Deliverables

* ✅ Raw dataset (`dataset_raw.csv`)
* ✅ Processed dataset (`dataset_processed.csv`)
* ✅ Trained models (`.pkl`)
* ✅ Word2Vec model
* ✅ Notebook (end-to-end pipeline)
* ✅ Requirements file

---

## ⚠️ Challenges & Solutions

| Challenge         | Solution                  |
| ----------------- | ------------------------- |
| Slang language    | Custom slang dictionary   |
| Class imbalance   | class_weight='balanced'   |
| Noisy labels      | Acknowledged + documented |
| Negation handling | Explicit preservation     |

---

## 📌 Limitations

* Labeling based on ratings (not manual)
* Limited handling of sarcasm
* Word2Vec performance depends on dataset size

---

## 🔮 Future Improvements

* Use deep learning (IndoBERT)
* Aspect-based sentiment analysis
* Real-time API deployment
* Larger dataset integration

---

## ⚖️ Ethics & Compliance

* Uses **publicly available data only**
* No personal data collected
* No scraping abuse (rate-limited)
* Academic use only

---

## 👨‍💻 Author

**Akmal Maulana**
AI / Data Enthusiast

---

## ⭐ Why This Project Matters

This project demonstrates:

* End-to-end ML pipeline design
* Real-world data handling
* Indonesian NLP challenges
* Production-thinking approach

---
