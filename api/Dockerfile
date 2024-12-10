FROM python:3.9-slim

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/api.py .
COPY api/gradient_boosting_model.joblib api/

CMD [ "fastapi", "run", "api.py" ]
