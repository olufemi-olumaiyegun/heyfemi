# Generated by Django 3.0.5 on 2020-06-03 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heyfemiapp', '0002_auto_20200603_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='heyfemiapp.Category'),
        ),
    ]