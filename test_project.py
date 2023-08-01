def test_home(client):
    response = client.get("/")
    assert b"<title>Warbler</title>" in response.data