FROM python:3.11-slim
WORKDIR /app

# Install system deps for psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8000
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/backend/src

# Use shell form so environment variables like $PORT are expanded at runtime
# fall back to 8000 when PORT is not set
CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app:app --bind 0.0.0.0:${PORT:-8000}