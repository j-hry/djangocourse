#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Mark migration 0003 as fake to avoid creator_id conflict
python manage.py migrate app 0003 --fake

# Run all other migrations
python manage.py migrate