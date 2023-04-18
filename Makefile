dev-install:
	poetry install --without prod

pc-config:
	pre-commit install --install-hooks

pc-after-commit:
	pre-commit run --from-ref origin/main --to-ref HEAD

pc-run-all:
	pre-commit run --all-files

pc-run:
	pre-commit run

tests:
	docker-compose exec todo_list tests

tests-local:
	doppler run -- pytest

bash:
	docker-compose exec enpyre_play bash

shell:
	doppler run -- python manage.py shell

migrations:
	doppler run -- python manage.py makemigrations

migrate:
	doppler run -- python manage.py migrate

collectstatic:
	doppler run -- python manage.py collectstatic --noinput
