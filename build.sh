#!/usr/bin/env bash
# esci se c'è un errore
set -o errexit

# installa le librerie
pip install -r requirements.txt

# raccogli i file statici (CSS admin)
python manage.py collectstatic --no-input

# applica le migrazioni al database
python manage.py migrate

# Crea il superuser in modo automatico (solo se non esiste già)
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@esempio.com', 'TuaPasswordSicura123')
    print('Superuser creato con successo!')
else:
    print('Superuser già esistente.')
EOF