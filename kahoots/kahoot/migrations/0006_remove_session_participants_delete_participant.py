# Generated by Django 4.0.3 on 2022-05-06 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kahoot', '0005_remove_quiz_questions_question_quiz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='participants',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
