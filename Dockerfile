FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# system dependencies needed for some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copy requirements first for better caching
COPY requirements.txt /app/

RUN python -m pip install --upgrade pip setuptools wheel \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# copy project
COPY . /app/

# collect static files (if configured)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# recommended production entry — change workers/bind as needed
CMD ["gunicorn", "Furniture_Web.wsgi:application", "--bind", "0.0.0.0:8000"]
