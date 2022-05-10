# Generated by Django 4.0.3 on 2022-05-10 14:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kahoot', '0009_game_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=30)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahoot.game')),
            ],
        ),
    ]
