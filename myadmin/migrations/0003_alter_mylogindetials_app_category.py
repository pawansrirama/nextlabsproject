# Generated by Django 4.2 on 2023-04-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_alter_mylogindetials_app_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylogindetials',
            name='app_category',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Eductional', 'Eductional'), ('Lifestyle', 'Lifestyle'), ('food', 'food'), ('common', 'common'), ('productivity', 'productivity')], default=1, max_length=255),
        ),
    ]