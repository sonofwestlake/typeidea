# Generated by Django 3.0.7 on 2020-07-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tag',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
