# Generated by Django 2.2.6 on 2019-10-31 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='cites',
            field=models.CharField(blank=True, choices=[('X', 'Cites of animal'), ('D', 'Cites D or (none)'), ('C', 'Cites C or III'), ('B', 'Cites B or II'), ('A', 'Cites A')], default='X', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='habitat',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='latinName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
