# Generated by Django 3.0.5 on 2020-06-03 17:15

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='heyfemiapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Author', models.CharField(max_length=255)),
                ('Date', models.DateTimeField()),
                ('Description', models.TextField()),
                ('Content', models.TextField()),
                ('Image', models.ImageField(blank=True, upload_to='gallery')),
                ('Category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='heyfemiapp.Category')),
            ],
        ),
    ]