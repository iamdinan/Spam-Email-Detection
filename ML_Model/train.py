# train.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# small dataset (for learning)
data = [
    ("win money now", "spam"),
    ("free iphone offer", "spam"),
    ("hello how are you", "not spam"),
    ("let's meet tomorrow", "not spam"),
    ("claim your prize", "spam"),
    ("project meeting at 5", "not spam")
]

texts = [x[0] for x in data]
labels = [x[1] for x in data]

# pipeline = vectorizer + model
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(texts, labels)

joblib.dump(model, "spam_model.pkl")

print("Model trained and saved!")