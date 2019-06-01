# Generated by Django 2.2.1 on 2019-06-01 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kosub', models.CharField(max_length=200)),
                ('ensub', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('EA', 'Easy'), ('MI', 'Middle'), ('HI', 'High')], default='MI', max_length=2)),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Sentence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]