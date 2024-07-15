# Generated by Django 5.0.6 on 2024-07-15 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(db_index=True, help_text="Enter book's year", verbose_name="Book's publication Year")),
                ('title', models.CharField(help_text="Enter book's title", max_length=150, verbose_name="Book's title")),
                ('category', models.CharField(choices=[('A', 'General Works'), ('B', 'Philosophy, Psychology, Religion'), ('C', 'Auxiliary Sciences of History'), ('D', 'World History and History of Europe, Asia, Africa, Australia, New Zealand, etc.'), ('E', 'History of America'), ('F', 'History of the Americas'), ('G', 'Geography, Anthropology, and Recreation'), ('H', 'Social Sciences'), ('J', 'Political Science'), ('K', 'Law'), ('L', 'Education'), ('M', 'Music'), ('N', 'Fine Arts'), ('P', 'Language and Literature'), ('Q', 'Science'), ('R', 'Medicine'), ('S', 'Agriculture'), ('T', 'Technology'), ('U', 'Military Science'), ('V', 'Naval Science'), ('Z', 'Bibliography, Library Science, and General Information Resources')], db_index=True, help_text="Enter book's LCC", max_length=1, verbose_name="Book's LCC")),
                ('language', models.CharField(choices=[('SPA', 'Spanish'), ('ENG', 'English'), ('FRE', 'French')], db_index=True, help_text="Enter book's language", max_length=3, verbose_name="Book's language")),
                ('authorship', models.ForeignKey(help_text="Enter author's name", on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.authors', verbose_name="Book's authorship")),
                ('publisher', models.ForeignKey(help_text="Enter publisher's name", on_delete=django.db.models.deletion.CASCADE, to='books.publishers', verbose_name="Book's publisher")),
            ],
        ),
    ]
