FROM rust:slim-bookworm

RUN apt update && apt install pip -y

RUN useradd -m appuser
USER appuser
WORKDIR /chatgpt-web
ENV PATH="/home/appuser/.local/bin:$PATH"
COPY . .
RUN pip install --break-system-packages --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8088", "main:server", "--timeout", "200", "--worker-class", "gevent"]
