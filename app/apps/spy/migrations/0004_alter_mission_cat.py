# Generated by Django 4.2.17 on 2025-06-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spy", "0003_remove_mission_complete_state_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mission",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="missions",
                to="spy.spycat",
            ),
        ),
    ]
