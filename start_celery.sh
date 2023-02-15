#!/bin/bash
echo "Criando atalho e inserindo no bashrc"
echo alias shell="'doppler run -- python manage.py shell'" >> ~/.bashrc
echo alias tests="'doppler run -- pytest'" >> ~/.bashrc

echo "Starting celery"
export COLUMNS=80

if test $ENVIRONMENT = 'production' ; then
CELERY_WORKER=1 celery -A enpyre_play worker -l info --without-heartbeat --without-gossip --without-mingle -Q $CELERY_DEFAULT_QUEUE
else
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A enpyre_play worker -l info -Q $CELERY_DEFAULT_QUEUE
fi
wait
