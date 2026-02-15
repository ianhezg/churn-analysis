FROM python:3.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

COPY models/model_c1.bin models/
COPY scripts/predict.py scripts/
COPY scripts/predict-test.py scripts/

WORKDIR /app
RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "scripts.predict:app"]