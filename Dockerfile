FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Ensure the entire project directory is copied for context
COPY . /code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
