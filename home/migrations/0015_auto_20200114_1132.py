# Generated by Django 2.2.9 on 2020-01-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_customtext_titledesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy', models.GenericIPAddressField(protocol='IPv4')),
            ],
        ),
        migrations.RemoveField(
            model_name='customtext',
            name='titledesign',
        ),
    ]
