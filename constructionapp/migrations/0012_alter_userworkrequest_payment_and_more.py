# Generated by Django 4.2.8 on 2023-12-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructionapp', '0011_alter_userworkrequest_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userworkrequest',
            name='payment',
            field=models.CharField(default='pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userworkrequest',
            name='status',
            field=models.CharField(default='pending', max_length=100, null=True),
        ),
    ]