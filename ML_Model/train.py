import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# load dataset
df = pd.read_csv("spam_mail_dataset.csv")

# drop missing values
df = df.dropna(subset=["Message"])

X = df["Message"]
y = df["Category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.2%}")
print(df["Category"].unique())

# Save model
joblib.dump(model, "spam_model.pkl")

print("Model saved!")