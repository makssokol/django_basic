# Generated by Django 3.0.3 on 2020-02-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200217_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artobject',
            name='short_desc',
        ),
        migrations.AddField(
            model_name='artobject',
            name='artist',
            field=models.CharField(blank=True, max_length=60, verbose_name='автор'),
        ),
    ]
