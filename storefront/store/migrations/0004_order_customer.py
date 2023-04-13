# Generated by Django 4.2 on 2023-04-13 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.PROTECT, to='store.customer'),
            preserve_default=False,
        ),
    ]
