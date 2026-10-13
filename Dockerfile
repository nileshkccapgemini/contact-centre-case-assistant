FROM python:3.14

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py mock_cases.py ./

USER 10001

CMD ["fastapi", "run", "main.py", "--port", "8000"]