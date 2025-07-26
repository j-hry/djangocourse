#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Force re-run the superuser migration
python manage.py migrate app 0001 --fake
python manage.py migrate app 0002

# Run all other migrations
python manage.py migrate