async def test_endpoint(client):
    resp = await client.get('/socket.io')

    assert resp.status_code == 200
