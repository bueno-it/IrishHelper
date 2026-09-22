FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD ["gunicorn", "irishHelper.wsgi:application", "--bind", "0.0.0.0:80", "--workers", "2"]
