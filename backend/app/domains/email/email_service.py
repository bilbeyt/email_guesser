import logging

from app.domains.email.email import EmailFormat, EmailFormatEnum
from app.domains.email.email_repository import EmailRepository


class EmailService:
    def __init__(self, repo: EmailRepository):
        self.repo = repo

    @staticmethod
    def _get_expected_email(full_name: str, domain: str, email_format: EmailFormatEnum) -> str:
        name_parts = full_name.split()
        first_name = name_parts[0]
        email = ""
        if email_format == EmailFormatEnum.FIRST_NAME_INITIAL_LAST_NAME:
            # in case name has multiple lastnames like Jane Doe Brilliant
            # then email should be jdoebrilliant@x.com if domain is x.com
            last_name = "".join(name_parts[1:])
            email = f"{first_name[0].lower()}{last_name.lower()}@{domain}"
        elif email_format == EmailFormatEnum.FIRST_NAME_LAST_NAME:
            email = f"{full_name.lower().replace(" ", "")}@{domain}"
        return email

    def get_email_by_full_name_and_domain(self, full_name: str, domain: str) -> str | None:
        email_format = self.repo.get_email_format_by_domain(domain)
        email = None
        if email_format is None:
            return email
        return self._get_expected_email(full_name, domain, email_format.format)

    def save_email_format_by_full_name_and_email(self, full_name: str, email: str) -> bool:
        email_parts = email.split("@")
        domain = email_parts[-1]
        if (
            self._get_expected_email(
                full_name, domain, EmailFormatEnum.FIRST_NAME_INITIAL_LAST_NAME
            )
            == email
        ):
            self.repo.create_email_format(
                EmailFormat(domain=domain, format=EmailFormatEnum.FIRST_NAME_INITIAL_LAST_NAME)
            )
        elif (
            self._get_expected_email(full_name, domain, EmailFormatEnum.FIRST_NAME_LAST_NAME)
            == email
        ):
            self.repo.create_email_format(
                EmailFormat(domain=domain, format=EmailFormatEnum.FIRST_NAME_LAST_NAME)
            )
        else:
            logging.info("Email format is not known: %s, %s", full_name, email)
            return False
        return True
