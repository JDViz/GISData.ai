# Generated by Django 4.2.5 on 2023-10-23 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk_management', '0004_alter_response_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='risk_management.question'),
        ),
    ]
