# Generated by Django 3.2.3 on 2021-06-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='fine',
        ),
    ]
