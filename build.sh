#!/usr/bin/env bash
# esci se c'è un errore
set -o errexit

# installa le librerie
pip install -r requirements.txt

# raccogli i file statici (CSS admin)
python manage.py collectstatic --no-input

# applica le migrazioni al database
python manage.py migrate