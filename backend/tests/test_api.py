from fastapi.testclient import TestClient
from app.main import app
from unittest import mock
from tests.utils import MockPsycopg2Connection
from app.domains.email.email import EmailFormatEnum


SUCCESS_CURSOR_RESPONSE = ("babbel.com", EmailFormatEnum.FIRST_NAME_INITIAL_LAST_NAME.value)


@mock.patch("psycopg2.connect", return_value=MockPsycopg2Connection(SUCCESS_CURSOR_RESPONSE))
def test_successful_email_guess(mocked_connect):
    client = TestClient(app)
    res = client.get("/api/email/guess?domain=babbel.com&fullname=Jane+Doe")
    assert res.status_code == 200
    assert res.json() == {"email": "jdoe@babbel.com"}


@mock.patch("psycopg2.connect", return_value=MockPsycopg2Connection(None))
def test_failed_email_guess(mocked_connect):
    mocked_connect.cursor.fetchone.return_value = None
    client = TestClient(app)
    res = client.get("/api/email/guess?domain=babbel.com&fullname=Jane+Doe")
    assert res.status_code == 400
