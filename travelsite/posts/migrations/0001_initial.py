# Generated by Django 4.0.6 on 2022-07-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=None)),
                ('is_published', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('growth', models.IntegerField(default=None)),
                ('weight', models.IntegerField(default=None)),
                ('price', models.IntegerField(default=None)),
                ('breast_size', models.IntegerField(default=None)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='product_image')),
            ],
        ),
    ]
