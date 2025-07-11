import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# تحميل بيانات التدريب
df = pd.read_csv("training_data.csv")

# تقسيم البيانات إلى ميزات ووسوم
X = df["message"]
y = df["label"]

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# بناء Pipeline: تحويل نص إلى أرقام + نموذج لوجستي
model_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

# تدريب النموذج
model_pipeline.fit(X_train, y_train)

# تقييم النموذج على بيانات الاختبار
y_pred = model_pipeline.predict(X_test)
print("دقة النموذج:", accuracy_score(y_test, y_pred))
print("\nالتقرير التفصيلي:")
print(classification_report(y_test, y_pred))

# حفظ النموذج
joblib.dump(model_pipeline, "app/model.pkl")
print("✅ تم حفظ النموذج في app/model.pkl")
