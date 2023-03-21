FROM python:alpine
RUN apk add --no-cache build-base libffi-dev
WORKDIR /chatgpt-web
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8088", "main:server", "--timeout", "200", "--worker-class", "gevent"]
