# Generated by Django 4.1 on 2022-10-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopmember', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopmember',
            name='user_email',
            field=models.CharField(default='', max_length=100, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='shopmemberdelete',
            name='user_email',
            field=models.CharField(default='', max_length=100, verbose_name='이메일'),
        ),
    ]
