# Generated by Django 3.1.2 on 2020-10-30 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='candidates',
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.election'),
        ),
    ]
