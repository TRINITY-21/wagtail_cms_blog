# Generated by Django 3.2.12 on 2022-02-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='intro',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
