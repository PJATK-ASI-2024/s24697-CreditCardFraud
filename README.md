# Wykrywanie oszustw związanych z kartami kredytowymi

## 1. Opis problemu biznesowego/technicznego

### Problem biznesowy

Oszustwa kartami kredytowymi powodują znaczące straty finansowe dla instytucji finansowych. Szybkie i skuteczne wykrywanie podejrzanych transakcji jest kluczowe, aby zminimalizować straty oraz zwiększyć bezpieczeństwo klientów.

### Cel

Celem projektu jest stworzenie modelu, który na podstawie danych transakcyjnych będzie w stanie odróżnić transakcje legalne od podejrzanych, co pozwala na wykrycie oszustwa na wczesnym etapie.

## 2. Źródło danych, charakterystka oraz uzasadnienie

- **Źródło danych**: Zbiór danych „Credit Card Fraud” wzięty z serwisu [Kaggle](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud/data).
- **Opis Cech**:
  - distance_from_home - odległość od miejsca zamieszkania właściciela karty.
  - distance_from_last_transaction - odległość od miejsca, w którym miała miejsce ostatnia transakcja.
  - ratio_to_median_purchase_price - stosunek ceny zakupu w danej transakcji do mediany ceny zakupu.
  - repeat_retailer - czy karta brała udział w transakcji u tego sprzedawcy.
  - used_chip - czy transakcja została przeprowadzona przy użyciu fizycznej karty kredytowej.
  - used_pin_number - czy transakcja została zrealizowana przy użyciu numeru PIN.
  - online_order - czy transakcja była zamówieniem online.
  - fraud - czy transakcja jest oszustwem.
- **Uzasadnienie wyboru**:
  - Zbiór danych zawiera oznaczenia transakcji legalnych i nielegalnych, co umożliwia trenowanie modelu.
  - Dane te odzwierciedlają rzeczywiste scenariusze oszustw.

### Diagram przepływu

![Graf](media/graph.svg)

## 3. Analiza danych

```Data columns (total 8 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   distance_from_home              50000 non-null  float64
 1   distance_from_last_transaction  50000 non-null  float64
 2   ratio_to_median_purchase_price  50000 non-null  float64
 3   repeat_retailer                 50000 non-null  float64
 4   used_chip                       50000 non-null  float64
 5   used_pin_number                 50000 non-null  float64
 6   online_order                    50000 non-null  float64
 7   fraud                           50000 non-null  float64
dtypes: float64(8)
memory usage: 3.1 MB
None
       distance_from_home  distance_from_last_transaction  ratio_to_median_purchase_price  repeat_retailer    used_chip  used_pin_number  online_order         fraud
count        50000.000000                    50000.000000                    50000.000000     50000.000000  50000.00000     50000.000000  50000.000000  50000.000000
mean            26.549348                        5.220660                        1.811345         0.881340      0.35056         0.100060      0.651740      0.086180
std             78.627567                       22.001490                        2.818171         0.323391      0.47715         0.300083      0.476424      0.280632
min              0.024144                        0.000539                        0.006125         0.000000      0.00000         0.000000      0.000000      0.000000
50%              9.907588                        1.018955                        0.990188         1.000000      0.00000         0.000000      1.000000      0.000000
75%             25.626905                        3.379200                        2.070817         1.000000      1.00000         0.000000      1.000000      0.000000
max          10632.723672                     1400.098234                       99.942349         1.000000      1.00000         1.000000      1.000000      1.000000
   distance_from_home  distance_from_last_transaction  ratio_to_median_purchase_price  repeat_retailer  used_chip  used_pin_number  online_order  fraud
0            0.929509                        1.296477                        0.361110              0.0        0.0              0.0           1.0    0.0
1            0.611179                        0.208295                        3.118884              0.0        0.0              0.0           1.0    0.0
2            3.956062                        0.529194                        1.579942              1.0        0.0              0.0           0.0    0.0
3           21.798902                        0.019399                       11.416909              1.0        0.0              0.0           0.0    0.0
4            3.310635                        1.707802                        2.028915              1.0        0.0              0.0           0.0    0.0
Brakujące wartości:
 distance_from_home                0
distance_from_last_transaction    0
ratio_to_median_purchase_price    0
repeat_retailer                   0
used_chip                         0
used_pin_number                   0
online_order                      0
fraud                             0
dtype: int64
```

## 4. Wybórz narzędzia do automatycznej analizy

W projekcie zastosowano narzędzie Sweetviz do automatycznej analizy danych, które generuje kompleksowy raport

## 5. Wybór modelu

```
Best pipeline: GradientBoostingClassifier(input_matrix, learning_rate=0.1, max_depth=4, max_features=0.55, min_samples_leaf=3, min_samples_split=10, n_estimators=100, subsample=0.9500000000000001)
Najlepszy model TPOT:
 Pipeline(steps=[('gradientboostingclassifier',
                 GradientBoostingClassifier(max_depth=4, max_features=0.55,
                                            min_samples_leaf=3,
                                            min_samples_split=10,
                                            subsample=0.9500000000000001))])
Dokładność modelu: 0.9996
Średni błąd bezwzględny: 0.0004
Raport klasyfikacji:
               precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     13700
         1.0       1.00      1.00      1.00      1300

    accuracy                           1.00     15000
   macro avg       1.00      1.00      1.00     15000
weighted avg       1.00      1.00      1.00     15000
```

## 5. Trenowanie wybranego modelu

```
Dokładność modelu: 0.99968
Średni błąd bezwzględny: 0.00032
Raport klasyfikacji:
               precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     11403
         1.0       1.00      1.00      1.00      1097

    accuracy                           1.00     12500
   macro avg       1.00      1.00      1.00     12500
weighted avg       1.00      1.00      1.00     12500
```
