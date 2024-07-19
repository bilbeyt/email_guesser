from unittest import mock
from tests.utils import MockPsycopg2Connection
from scripts.load_fixture import run


DATA = """
{
    "Jane Doe": "jdoe@babbel.com",
    "Tolga Bilbey": "tbilbey@linkedin.com"
}
"""

@mock.patch('scripts.load_fixture.create_table')
@mock.patch("psycopg2.connect", return_value=MockPsycopg2Connection(None))
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data=DATA)
def test_fixture_load(mocked_create_table, mocked_connect, mocked_open):
    run()
    mocked_create_table.assert_called_once()
    assert mocked_connect.call_count == 2
    mocked_open.assert_called_once()



