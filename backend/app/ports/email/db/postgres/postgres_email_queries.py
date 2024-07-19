INSERT_EMAIL_FORMAT_QUERY = """
    INSERT INTO email_formats(domain, format) VALUES(%s, %s)
    ON CONFLICT (domain) DO NOTHING
"""

GET_EMAIL_FORMAT_BY_DOMAIN_QUERY = """
    SELECT * FROM email_formats WHERE domain = %s
"""

CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS email_formats(
        domain varchar(255) primary key,
        format integer
    );
"""
