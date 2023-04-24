from abc import ABC, abstractmethod
import re


class Validator(ABC):
    DEFAULT_NAME_LEN_THRESHOLD = 200
    LOW_YEAR_THRESHOLD = 1895


    @abstractmethod
    def validate(self, value: str) -> bool:
        pass


class ValidateName(Validator):
    def validate(self, value: str) -> bool:
        len_threshold = self.DEFAULT_NAME_LEN_THRESHOLD
        len_value = len(value)
        is_len_appropriate = len_value < len_threshold
        is_only_spaces_or_tabs = value.count(" ") + value.count("\t") == len_value
        return is_len_appropriate and not is_only_spaces_or_tabs

class ValidateYear(Validator):
    def validate(self, value: str) -> bool:
        is_digit = value.isdigit()
        if is_digit:
            value = int(value)
            if value >= self.LOW_YEAR_THRESHOLD:
                return True
        else:
            return False

class ValidateDirector(Validator):
    def validate(self, value: str) -> bool:
        is_dir_valid = value.replace(" ", "").replace("-", "").replace(".", "").isalpha()
        return is_dir_valid


class ValidateRank(Validator):
    def validate(self, value: str) -> bool:
        pattern_for_floats = "^[0-9]+\.[0-9]+$"
        try:
            is_rank_valid_re = re.match(pattern_for_floats, value).string == value
        except AttributeError:
            is_rank_valid_re = None
        return is_rank_valid_re