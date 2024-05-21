# Generated by Django 4.2.7 on 2024-05-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_review_user_alter_review_book_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_imgs/'),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
