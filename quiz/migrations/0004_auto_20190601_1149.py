# Generated by Django 2.2.1 on 2019-06-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_history_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='level',
        ),
        migrations.RemoveField(
            model_name='history',
            name='user',
        ),
        migrations.AlterField(
            model_name='sentence',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
