# Generated by Django 4.0.5 on 2022-07-24 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_productrating_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productrating',
            old_name='ProductId',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='productrating',
            old_name='UserId',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='productrating',
            name='created_at',
        ),
    ]
