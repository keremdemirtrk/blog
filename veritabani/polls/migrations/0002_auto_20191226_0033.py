# Generated by Django 3.0.1 on 2019-12-25 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
