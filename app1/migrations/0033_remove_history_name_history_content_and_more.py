# Generated by Django 4.1.2 on 2022-11-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_remove_profile_personal_statement_personalstatement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='name',
        ),
        migrations.AddField(
            model_name='history',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='PersonalStatement',
        ),
    ]
