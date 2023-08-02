import re
from pprint import pprint


class ValidateEmail:
    __RE_VALIDATE = r"^[a-z0-9]+([._-][a-z0-9]+)*@[a-z0-9-]+(\.[a-z]{2,})+$"


    def __init__(self, email: str) -> None:
        self.__validate_email(email)
        self.email = email


    @classmethod
    def __validate_email(cls, email: str) -> None:
        if not re.match(cls.__RE_VALIDATE, email):
            raise ValueError("Invalid email address")


test_email = ['abc-@mail.com',              # Invalid email prefixes
              'abc..def@mail.com',          # Invalid email prefixes
              '.abc@mail.com',              # Invalid email prefixes
              'abc#def@mail.com',           # Invalid email prefixes
              'abc-d@mail.com',             # Valid email prefixes
              'abc.def@mail.com',           # Valid email prefixes
              'abc@mail.com',               # Valid email prefixes
              'abc_def@mail.com',           # Valid email prefixes
              'abc.def@mail.c',             # Invalid email domains
              'abc.def@mail#archive.com',   # Invalid email domains
              'abc.def@mail',               # Invalid email domains
              'abc.def@mail..com',          # Invalid email domains
              'abc.def@mail.cc',            # Valid email domains
              'abc.def@mail-archive.com',   # Valid email domains
              'abc.def@mail.org',           # Valid email domains
              'abc.def@mail.com',           # Valid email domains
              'abc.defmail.com'             # Invalid not available @
              ]

invalid = list()
valid = list()

for email in test_email:
    try:
        ValidateEmail(email)
        valid.append(email)
    except ValueError:
        invalid.append(email)

pprint(invalid)
pprint(valid)