import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, classification_report
import joblib
import os



tpot_data = pd.read_csv('data/data.csv', sep=',', dtype=np.float64)
features = tpot_data.drop('fraud', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['fraud'], random_state=42)

exported_pipeline = GradientBoostingClassifier(learning_rate=0.1, max_depth=4, max_features=0.55, min_samples_leaf=3, min_samples_split=10, n_estimators=100, subsample=0.9500000000000001)

if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

print("Dokładność modelu:", accuracy_score(testing_target, results))
print("Średni błąd bezwzględny:", mean_absolute_error(testing_target, results))
print("Raport klasyfikacji:\n", classification_report(testing_target, results))

os.makedirs('api', exist_ok=True)
joblib.dump(exported_pipeline, 'api/gradient_boosting_model.joblib')