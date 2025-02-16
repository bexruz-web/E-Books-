# Generated by Django 5.1.6 on 2025-02-16 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_flashsale_userbookview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashsale',
            old_name='product',
            new_name='book',
        ),
        migrations.AlterUniqueTogether(
            name='flashsale',
            unique_together={('book', 'start_time', 'end_time')},
        ),
    ]
