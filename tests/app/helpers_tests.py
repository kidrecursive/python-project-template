from app.helpers import get_greeting

def test_get_greeting():
    """
    it should return a customized greeting
    """
    greeting = get_greeting("CRW")
    assert greeting == "Hello, CRW!"
    