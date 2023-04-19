# Generated by Django 4.2 on 2023-04-15 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='myLoginDetials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='app_images/')),
                ('app_name', models.CharField(max_length=100)),
                ('app_link', models.CharField(max_length=200)),
                ('points_amount', models.IntegerField()),
                ('app_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myadmin.category')),
                ('sub_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myadmin.subcategory')),
            ],
        ),
    ]
