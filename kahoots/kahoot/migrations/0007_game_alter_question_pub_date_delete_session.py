# Generated by Django 4.0.3 on 2022-05-10 13:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kahoot', '0006_remove_session_participants_delete_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kahoot.quiz')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]