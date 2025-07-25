# Add dependency
poetry add some-package

# Regenerate requirements.txt
poetry export -f requirements.txt --output requirements.txt --without-hashes

# Commit both files
git add pyproject.toml poetry.lock requirements.txt
git commit -m "Add some-package dependency"