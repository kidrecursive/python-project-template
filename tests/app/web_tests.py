from app.web import app

client = app.test_client()

def test_hello_name():
    """
    it should output a customized greeting: hello <name>
    """
    res = client.get('/hello/crw')
    assert res.status_code == 200
    print(res.data)
    assert res.data == b'Hello, crw!'
    