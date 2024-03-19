from django.core.exceptions import ValidationError
from django.db import models


def validate_file_size(file):
    max_size_kb = 50

    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Files can not be larger than {max_size_kb}KB")


def percentage_validator(value):
    if not (0 <= value <= 100):
        raise models.ValidationError(
            "Validation error: Percentage must be between 0 and 100"
        )