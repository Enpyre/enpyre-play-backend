import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(scope='function')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        from scripts import CleanDB, PopulateDB

        CleanDB.run()
        PopulateDB.run()


@pytest.fixture
def user(db):
    return get_user_model().objects.get(email='test@enpyre.com.br')


@pytest.fixture
def authenticated_client(user, client: APIClient):
    client.force_authenticate(user=user)
    return client
