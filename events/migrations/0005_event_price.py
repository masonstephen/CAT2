# Generated by Django 5.1.4 on 2024-12-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_attendee_events_attendee_user_organizer_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]