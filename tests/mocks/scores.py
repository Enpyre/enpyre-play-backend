import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_compute_score_task(mocker: MockFixture):
    return mocker.patch('enpyre_play.scores.tasks.compute_score')


@pytest.fixture
def mock_compute_global_score_task(mocker: MockFixture):
    return mocker.patch('enpyre_play.scores.tasks.compute_global_score')


@pytest.fixture
def mock_compute_yearly_score_task(mocker: MockFixture):
    return mocker.patch('enpyre_play.scores.tasks.compute_yearly_score')


@pytest.fixture
def mock_compute_monthly_score_task(mocker: MockFixture):
    return mocker.patch('enpyre_play.scores.tasks.compute_monthly_score')


@pytest.fixture
def mock_compute_weekly_score_task(mocker: MockFixture):
    return mocker.patch('enpyre_play.scores.tasks.compute_weekly_score')


@pytest.fixture
def mock_all_compute_score_tasks(
    mock_compute_score_task,
    mock_compute_global_score_task,
    mock_compute_yearly_score_task,
    mock_compute_monthly_score_task,
    mock_compute_weekly_score_task,
):
    return (
        mock_compute_score_task,
        mock_compute_global_score_task,
        mock_compute_yearly_score_task,
        mock_compute_monthly_score_task,
        mock_compute_weekly_score_task,
    )
