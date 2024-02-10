@echo off
poetry config virtualenvs.in-project true
poetry install --no-root
py -c "import os; os.remove('poetry.lock')"