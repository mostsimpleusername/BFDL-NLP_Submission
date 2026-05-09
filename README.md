# 📈 Indonesian Stock Investment App Sentiment Analysis

Sentiment analysis project for Indonesian stock investment and brokerage applications using Machine Learning, Deep Learning, and Transformer-based models.

---

# 📌 Project Overview

This project aims to analyze user sentiment toward Indonesian investment and brokerage applications based on reviews collected from the Google Play Store.

The dataset was independently collected through a scraping process using Python and the `google-play-scraper` library.

The project implements several approaches:

- Traditional Machine Learning
- Deep Learning
- Transformer-based NLP (IndoBERT)

---

# 🎯 Objectives

The main objectives of this project are:

- Collect review datasets from Indonesian investment applications
- Perform Indonesian text preprocessing
- Build sentiment classification models
- Compare multiple machine learning and deep learning approaches
- Implement sentiment inference on unseen data

---

# 📱 Applications Analyzed

The dataset consists of reviews from several popular Indonesian investment platforms:

| Application | Play Store ID |
|---|---|
| Ajaib | `ajaib.co.id` |
| Bibit | `com.bibit.bibitid` |
| Stockbit | `com.stockbit.android` |
| IPOT | `com.indopremier.ipot` |

---

# 📊 Dataset Information

| Information | Value |
|---|---|
| Data Source | Google Play Store |
| Total Samples | 10,000+ reviews |
| Language | Indonesian |
| Labels | Positive, Neutral, Negative |
| Collection Method | Web Scraping |

---

# ⚠️ Ethical Considerations

This project follows ethical data collection practices:

- Uses publicly available Google Play Store reviews
- Does not collect sensitive user information
- Avoids excessive scraping requests
- Includes delay mechanisms during scraping
- Used strictly for educational and research purposes

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Main Libraries
- pandas
- numpy
- scikit-learn
- tensorflow
- transformers
- torch
- nltk
- matplotlib
- seaborn
- google-play-scraper
- wordcloud

---

# 📂 Project Structure

```bash
sentiment-analysis-sekuritas/
│
├── data/
│   ├── reviews_sekuritas.csv
│   ├── cleaned_reviews.csv
│
├── notebooks/
│   ├── sentiment_analysis.ipynb
│
├── models/
│   ├── random_forest.pkl
│   ├── indobert/
│
├── images/
│   ├── confusion_matrix.png
│   ├── wordcloud_positive.png
│   ├── wordcloud_negative.png
│
├── nlp_submission_scraping.py
├── requirements.txt
├── README.md
└── scrape.py
```

---

# 🔎 Data Scraping

The dataset was collected using:

```python
from google_play_scraper import reviews
```

Main scraping configuration:

```python
apps = {
    "Ajaib": "ajaib.co.id",
    "Bibit": "com.bibit.bibitid",
    "Stockbit": "com.stockbit.android",
    "IPOT": "com.indopremier.ipot"
}
```

Target reviews per application:

```python
TARGET_PER_APP = 4000
```

Scraping strategy:

- Collect latest reviews (`Sort.NEWEST`)
- Use continuation tokens for pagination
- Add request delays to avoid spam requests
- Store review metadata for analysis

---

# 📋 Dataset Columns

| Column | Description |
|---|---|
| app | Application name |
| reviewId | Review ID |
| userName | Username |
| content | Review text |
| score | User rating |
| thumbsUpCount | Number of likes |
| at | Review timestamp |
| appVersion | Application version |

---

# 🧹 Text Preprocessing

The preprocessing pipeline includes:

## 1. Missing Value Removal
Remove empty or null reviews.

## 2. Duplicate Removal
Remove duplicate reviews.

## 3. Regex Cleaning
Remove:

- URLs
- Mentions
- Hashtags
- Numbers
- Emojis
- Symbols
- Special characters

## 4. Case Folding
Convert all text to lowercase.

## 5. Slang Normalization
Convert informal Indonesian words into formal words.

Example:

| Slang | Formal |
|---|---|
| gk | tidak |
| bgt | banget |
| tdk | tidak |

## 6. Tokenization
Split text into tokens.

## 7. Stopword Removal
Remove common non-informative words.

---

# 🏷️ Labeling Strategy

Sentiment labels are generated based on user ratings:

| Rating | Label |
|---|---|
| 4-5 | Positive |
| 3 | Neutral |
| 1-2 | Negative |

---

# ⚙️ Feature Extraction

## TF-IDF
Used for traditional Machine Learning models.

```python
TfidfVectorizer(
    max_features=25000,
    ngram_range=(1,2),
    min_df=3,
    max_df=0.9,
    sublinear_tf=True,
    norm='l2'
)
```

## Word Embedding
Used for Deep Learning models.

## Transformer Embedding
Used pretrained IndoBERT embeddings.

---

# 🤖 Models Used

## Machine Learning Models

### Logistic Regression
Used as a baseline model.

### Support Vector Machine (SVM)
Used for high-dimensional text classification.

### Random Forest
Used to capture non-linear patterns.

## Deep Learning Models

### Bi-LSTM
Used to understand sequential text patterns.

### IndoBERT
Transformer-based pretrained Indonesian language model.

---

# 📈 Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📊 Model Results

| Scheme | Algorithm | Feature Extraction | Split Ratio | Test Accuracy |
|---|---|---|---|---|
| 1 | Logistic Regression | TF-IDF | 80:20 | 85.28% |
| 2 | SVM | TF-IDF | 80:20 | 83%+ |
| 3 | Random Forest | TF-IDF | 80:20 | 85.44% |
| 4 | Bi-LSTM | Embedding | 70:30 | 82%+ |
| 5 | IndoBERT | Transformer | 80:20 | 86.67% |

---

# 🧠 Key Findings

- IndoBERT achieved the best overall performance.
- TF-IDF + Random Forest produced stable and lightweight results.
- The neutral class was the most difficult to classify.
- Many reviews contained mixed sentiments.
- Informal Indonesian language significantly affected model performance.

---

# ❌ Challenges

Main challenges encountered during development:

- Imbalanced dataset
- Noisy real-world text
- Indonesian slang language
- Ambiguous sentiment
- Sarcasm
- Negation context handling

---

# 🔬 Error Analysis

Traditional TF-IDF-based models struggled to understand contextual negation.

Example:

```text
"fiturnya tidak terlalu membantu"
```

The word "membantu" (helpful) was often interpreted as positive despite the negative context.

Transformer-based models such as IndoBERT performed better in handling contextual meaning.

---

# 🚀 Inference Example

## Input

```text
"aplikasinya bagus tapi sering error"
```

## Output

```text
negative
```

---

# 📉 Visualization

The project includes several visualizations:

- Sentiment distribution
- Word clouds
- Confusion matrix
- Model accuracy comparison

---

# ▶️ How to Run

## 1. Clone Repository

```bash
git clone https://github.com/your-username/sentiment-analysis-sekuritas.git
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Scraping Script

```bash
python nlp_submission_scraping.py
```

## 4. Open Jupyter Notebook

```bash
jupyter notebook
```

---

# 📦 Requirements

```text
pandas
numpy
scikit-learn
tensorflow
transformers
torch
nltk
matplotlib
seaborn
wordcloud
google-play-scraper
```

---

# 📚 Learning Outcomes

Through this project, I learned:

- Indonesian NLP preprocessing
- Sentiment analysis workflow
- TF-IDF feature extraction
- Deep Learning for NLP
- Transformer-based NLP
- Model evaluation
- Error analysis
- Data scraping
- Text classification
- Handling noisy real-world datasets
- Hyperparameter experimentation
- Comparing ML vs DL vs Transformer models

---

# 📝 Reviewer Feedback & Reflection

This project successfully fulfilled several important requirements:

✅ Implemented Deep Learning models

✅ Used more than 10,000 data samples

✅ Applied multi-class sentiment classification

✅ Conducted multiple training experiments

✅ Performed sentiment inference on unseen data

However, the reviewer also provided several improvement suggestions:

- Test accuracy has not yet exceeded 92%
- Text preprocessing can still be optimized
- Rating-based labeling may introduce bias
- Models still struggle with ambiguous and negated sentences

From this feedback, several important insights were gained:

- Real-world datasets contain significant noise
- Label quality strongly affects model performance
- Transformer-based models outperform traditional approaches in contextual understanding
- Error analysis is essential to understand model limitations
- NLP optimization depends not only on models but also on preprocessing quality and labeling strategy

The reviewer feedback became an important learning resource for improving future NLP projects.

---

# 🔮 Future Improvements

Based on reviewer suggestions, several future improvements can be implemented:

## 🔹 Improve Model Performance

- Perform extensive hyperparameter tuning
- Fine-tune IndoBERT using optimized learning rates
- Apply early stopping and regularization
- Use class weighting for imbalanced datasets
- Implement cross-validation to reduce overfitting

## 🔹 Advanced Text Preprocessing

- Improve slang normalization
- Add emoji handling
- Compare stemming vs lemmatization
- Filter noisy reviews
- Handle negation context more effectively
- Apply text augmentation techniques

## 🔹 Better Feature Extraction

Additional feature extraction methods:

- Word2Vec
- FastText
- GloVe
- Contextual embeddings

## 🔹 Better Labeling Strategy

- Manual relabeling for ambiguous samples
- Semi-supervised labeling
- BERT-assisted labeling
- Reduce rating-based labeling bias

## 🔹 Experiment Tracking

- MLflow
- Weights & Biases
- Hyperparameter logging

## 🔹 Explainable AI (XAI)

Improve model interpretability using:

- SHAP
- LIME
- PCA visualization
- t-SNE visualization

## 🔹 Better Evaluation

- Per-class precision
- Per-class recall
- Per-class F1-score
- Confusion matrix analysis
- Detailed error analysis

## 🔹 Deployment

- REST API deployment
- Streamlit dashboard
- Real-time sentiment analysis
- Docker containerization

---

# 👨‍💻 Author

Akmal Maulana

---

# 📜 License

This project was created for educational and research purposes.

---

# ⭐ Acknowledgements

- Google Play Store
- Hugging Face
- TensorFlow
- Scikit-learn
- Dicoding Indonesia

