def test_status(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}
