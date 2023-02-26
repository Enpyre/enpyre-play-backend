import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .mocks import *  # noqa


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(scope='function')
def django_db_setup(django_db_setup, django_db_blocker, mock_all_compute_score_tasks):
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


@pytest.fixture
def user_shared_public(db):
    return get_user_model().objects.get(email='test-shared-public@enpyre.com.br')


@pytest.fixture
def client_user_shared_public(user_shared_public, client: APIClient):
    client.force_authenticate(user=user_shared_public)
    return client


@pytest.fixture
def user_shared(db):
    return get_user_model().objects.get(email='test-shared@enpyre.com.br')


@pytest.fixture
def client_user_shared(user_shared, client: APIClient):
    client.force_authenticate(user=user_shared)
    return client


@pytest.fixture
def user_public(db):
    return get_user_model().objects.get(email='test-public@enpyre.com.br')


@pytest.fixture
def client_user_public(user_public, client: APIClient):
    client.force_authenticate(user=user_public)
    return client
