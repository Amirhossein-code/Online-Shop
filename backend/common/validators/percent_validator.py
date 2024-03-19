from django.db import models


def percentage_validator(value):
    if not (0 <= value <= 100):
        raise models.ValidationError(
            "Validation error: Percentage must be between 0 and 100"
        )
