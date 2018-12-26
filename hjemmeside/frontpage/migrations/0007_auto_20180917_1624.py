# Generated by Django 2.1 on 2018-09-17 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontpage', '0006_auto_20180917_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='M2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttid', models.CharField(max_length=255)),
                ('sluttid', models.CharField(max_length=255)),
                ('columnlen', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='M3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttid', models.CharField(max_length=255)),
                ('sluttid', models.CharField(max_length=255)),
                ('columnlen', models.IntegerField()),
            ],
        ),

        migrations.AddField(
            model_name='m3',
            name='usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='m2',
            name='usr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
