# Generated by Django 3.2.6 on 2022-05-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='speech',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
