# Generated by Django 5.2.1 on 2025-05-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='caption',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.CharField(default='Uncategorized', max_length=100),
        ),
    ]
