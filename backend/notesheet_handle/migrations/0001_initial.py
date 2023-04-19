# Generated by Django 4.1.7 on 2023-04-19 06:46

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
            name="FacultyDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ns_id", models.IntegerField()),
                ("employee_id", models.CharField(max_length=20)),
                ("sender_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="NoteSheet",
            fields=[
                ("ppk", models.IntegerField(primary_key=True, serialize=False)),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
                ("subject", models.TextField()),
                ("school", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("objective", models.TextField()),
                ("proposal_details", models.TextField()),
                ("proposal_submitted_by", models.CharField(max_length=255)),
                ("proposal_submitted_by_1", models.CharField(max_length=255)),
                ("receiver_1", models.CharField(max_length=255)),
                ("receiver_2", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="FacultyProfile",
            fields=[
                (
                    "employee_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("designation", models.CharField(max_length=255)),
                ("school", models.CharField(max_length=255)),
                ("department", models.CharField(default="cse", max_length=255)),
                ("mobile_number", models.IntegerField()),
                ("email_address", models.CharField(max_length=255)),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
