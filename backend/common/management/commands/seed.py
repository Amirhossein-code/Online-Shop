# api/management/commands/seed.py
from django.core.management.base import BaseCommand
from model_bakery import baker
from store.models import Product, Category


class Command(BaseCommand):
    help = "Generate and save fake data for models"

    def handle(self, *args, **options):
        # Generate a list of fake categories
        # fake_category_categories_list = baker.make(Category, _quantity=100)
        # Generate a list of fake Products
        fake_products_list = baker.make(Product, _quantity=500)

        # Save the fake data to the database
        # Category.objects.bulk_create(fake_category_categories_list)
        Product.objects.bulk_create(fake_products_list)

        self.stdout.write(
            self.style.SUCCESS("Successfully generated and saved fake data for models")
        )
