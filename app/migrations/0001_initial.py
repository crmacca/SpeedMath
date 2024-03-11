# Generated by Django 5.0.1 on 2024-03-08 02:23

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quizId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quizCompleted', models.BooleanField(default=False)),
                ('quizCorrectlyCompleted', models.PositiveIntegerField(default=0)),
                ('quizQuestions', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]