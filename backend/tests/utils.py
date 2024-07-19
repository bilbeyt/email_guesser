from unittest import mock


class MockCursor:

    def __init__(self, return_value):
        self.return_value = return_value

    def execute(self, query, params=None):
        pass

    def fetchone(self):
        return self.return_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockPsycopg2Connection:
    def __init__(self, cursor_return_value):
        self.cursor_obj = MockCursor(cursor_return_value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def cursor(self):
        return self.cursor_obj
