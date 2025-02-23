# Generated by Django 5.1.4 on 2025-02-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="production_cost",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
