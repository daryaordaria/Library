# Generated by Django 4.1.5 on 2023-01-19 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookie', '0003_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='book_name',
            new_name='name_book',
        ),
    ]
