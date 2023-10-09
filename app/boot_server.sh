#!/bin/sh
nginx
gunicorn app:app -b 127.0.0.1:5000 --workers 1 --worker-class gthread --threads 1 --log-level info
