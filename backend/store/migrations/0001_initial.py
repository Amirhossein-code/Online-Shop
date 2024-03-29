# Generated by Django 5.0.3 on 2024-03-29 10:05

import autoslug.fields
import common.utils.custom_slug_utils
import common.validators.file_size_validator
import common.validators.percent_validator
import common.validators.rating_validator
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title', slugify=common.utils.custom_slug_utils.custom_slugify, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/category/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/profile')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('full_address', models.CharField(max_length=550)),
                ('main', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_status', models.CharField(choices=[('Shipment failed', 'Shipment failed'), ('Shipment success', 'Shipment success'), ('Order is being processed', 'Order is being processed')], default='Order is being processed', max_length=30)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title', slugify=common.utils.custom_slug_utils.custom_slugify, unique=True)),
                ('discount_percent', models.IntegerField(blank=True, default=0, null=True, validators=[common.validators.percent_validator.percentage_validator])),
                ('original_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('unit_price', models.PositiveBigIntegerField()),
                ('inventory', models.PositiveIntegerField(default=0)),
                ('is_hot', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('New Arrival', 'New Arrival'), ('Out of Stock', 'Out of Stock'), ('Available', 'Available'), ('Not Available', 'Not Available'), ('Discounted', 'Discounted')], default='New Arrival', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('unit_price', models.PositiveBigIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='store/images', validators=[common.validators.file_size_validator.validate_file_size])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[common.validators.rating_validator.validate_rating])),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('not_approved', 'Not Approved')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'unique_together': {('cart', 'product')},
            },
        ),
    ]
