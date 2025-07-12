from utils.validators import validate_email, validate_phone

def test_validate_email_valid():
    assert validate_email("test@example.com") is True

def test_validate_email_invalid():
    assert validate_email("not-an-email") is False

def test_validate_phone_valid():
    assert validate_phone("+380123456789") is True

def test_validate_phone_invalid():
    assert validate_phone("12345") is False
