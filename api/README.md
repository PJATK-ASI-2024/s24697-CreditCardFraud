# REST API do Modelu napisane przy użyciu fastAPI

## Jak uruchomić aplikację

### Kontener:

```
docker build -t rest-api-model -f ./api/Dockerfile .
docker run -d -p 8000:8000 rest-api-model
```

### Serwis REST API:

```
pip install -r ./api/requirements.txt
python dev api/api.py
```

### Testowanie aplikacji poprzez curl:

```
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "distance_from_home": 5.5,
  "distance_from_last_transaction": 12.3,
  "ratio_to_median_purchase_price": 0.8,
  "repeat_retailer": 1,
  "used_chip": 0,
  "used_pin_number": 1,
  "online_order": 0
}'
```
