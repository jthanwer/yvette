# Generated by Django 2.1.4 on 2019-03-14 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colocation',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users_app.Profile'),
        ),
    ]
