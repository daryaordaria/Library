# Generated by Django 4.1.5 on 2023-01-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Genres')),
                ('field_name', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('field_name', models.SlugField(max_length=100)),
                ('book_cover', models.ImageField(blank=True, null=True, upload_to='img')),
                ('author_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('book_file', models.FileField(upload_to='pdf')),
                ('best_books', models.BooleanField(default=False)),
                ('java_script', models.BooleanField(default=False)),
                ('html_css', models.BooleanField(default=False)),
                ('genre', models.ManyToManyField(related_name='books', to='bookie.genre')),
            ],
        ),
    ]
