# Generated by Django 2.2.9 on 2020-01-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_table_testdemo_testdemo1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
