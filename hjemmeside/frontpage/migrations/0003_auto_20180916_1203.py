# Generated by Django 2.1 on 2018-09-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_m1_columnlen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='m1',
            old_name='tid',
            new_name='sluttid',
        ),
        migrations.AddField(
            model_name='m1',
            name='starttid',
            field=models.CharField(default='13:00', max_length=255),
            preserve_default=False,
        ),
    ]
