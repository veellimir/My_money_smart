import re

from .exceptions import (
    EXCEPTION_ERROR_PASSWORD,
    EXCEPTION_QUANTITY_PASSWORD,
    EXCEPTION_LETTERS_PASSWORD,
    EXCEPTION_DIGIT_PASSWORD,
    EXCEPTION_INCORRECT_EMAIL,
)


def validate_username(username: str) -> None:
    if not re.match(r"^[a-zA-Z]{4,20}$", username):
        raise EXCEPTION_ERROR_PASSWORD


def validate_password(password: str) -> None:
    if len(password) < 6:
        raise EXCEPTION_QUANTITY_PASSWORD
    if not re.search(r"[A-Za-z]", password):
        raise EXCEPTION_LETTERS_PASSWORD
    if not re.search(r"\d", password):
        raise EXCEPTION_DIGIT_PASSWORD


def validate_email(email: str) -> None:
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        raise EXCEPTION_INCORRECT_EMAIL
