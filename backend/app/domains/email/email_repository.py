import abc

from app.domains.email.email import EmailFormat


class EmailRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_email_format_by_domain(self, domain: str) -> EmailFormat | None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_email_format(self, email_format: EmailFormat) -> bool:
        raise NotImplementedError
