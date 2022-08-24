# Generated by Django 4.1 on 2022-08-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCS_task', '0002_translation_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='description',
            field=models.TextField(default='some description'),
        ),
        migrations.AlterField(
            model_name='translation',
            name='transaction_id',
            field=models.CharField(default='some id', max_length=255),
        ),
    ]