#!/bin/bash
echo "Criando atalho e inserindo no bashrc"
echo alias shell="'doppler run -- python manage.py shell'" >> ~/.bashrc
echo alias tests="'doppler run -- pytest'" >> ~/.bashrc

echo "Esperando o banco de dados conectar"
postgres_ready() {
python3 << END
import sys
import psycopg2
import traceback
from decouple import config
try:
    conn = psycopg2.connect(
        dbname=config('DB_NAME', default='enpyre_db'),
        user=config('DB_USER', default='enpyre'),
        password=config('DB_PASSWORD', default='enpyre'),
        host=config('DB_HOST', default='enpyre_postgres'),
        port=config('DB_PORT', default=5432, cast=int),
    )
except psycopg2.OperationalError:
    traceback.print_exc()
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "PostgreSQL não está disponível ainda - Espere..."
  sleep 1
done

echo "Starting celery"
export COLUMNS=80

if test $ENVIRONMENT = 'production' ; then
CELERY_WORKER=1 celery -A enpyre_play worker -l info --without-heartbeat --without-gossip --without-mingle -Q $CELERY_DEFAULT_QUEUE
else
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A enpyre_play worker -l info -Q $CELERY_DEFAULT_QUEUE
fi
wait
