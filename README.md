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

