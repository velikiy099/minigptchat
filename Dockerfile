# --- Python application stage ---
FROM python:3.11-alpine

WORKDIR /app

COPY ./app/requirements.txt /app/
# Install necessary libraries and tools
RUN apk update \
    && apk add gcc libpq-dev nginx \
    && pip install --no-cache-dir -r requirements.txt

COPY ./app/ /app/
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["/app/boot_server.sh"]
