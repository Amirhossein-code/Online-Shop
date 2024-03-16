from django.utils.text import slugify


def custom_slugify(value):
    # allows persian text slugification
    return slugify(value, allow_unicode=True)
