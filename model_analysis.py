# Importowanie potrzebnych bibliotek
import pandas as pd
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, classification_report

data = pd.read_csv('./data/data.csv')


X = data.drop(columns='fraud')
y = data['fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)

print("Najlepszy model TPOT:\n", tpot.fitted_pipeline_)

y_pred = tpot.predict(X_test)
print("Dokładność modelu:", accuracy_score(y_test, y_pred))
print("Średni błąd bezwzględny:", mean_absolute_error(y_test, y_pred))
print("Raport klasyfikacji:\n", classification_report(y_test, y_pred))

# tpot.export('model.py')  # Eksport kodu do modelu