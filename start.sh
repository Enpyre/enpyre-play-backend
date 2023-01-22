#!/bin/bash
echo "Criando atalho e inserindo no bashrc"
echo alias shell="'doppler run -- python manage.py shell'" >> ~/.bashrc
echo alias test="'doppler run -- pytest'" >> ~/.bashrc
# echo alias shell="'python manage.py shell'" >> ~/.bashrc
# echo alias test="'pytest'" >> ~/.bashrc

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

echo "Rodando as migrações"
python manage.py migrate

echo "Rodando o servidor"
if test $ENVIRONMENT = 'development' ; then
  gunicorn enpyre_play.wsgi -b 0.0.0.0:8000 --reload --log-level DEBUG --workers 1 --graceful-timeout 0
else
  gunicorn enpyre_play.wsgi -b 0.0.0.0:8000 --log-level INFO --workers 2 --graceful-timeout 60
fi
