# Generated by Django 4.2.7 on 2023-11-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
