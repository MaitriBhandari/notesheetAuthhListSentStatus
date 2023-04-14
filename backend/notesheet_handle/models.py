from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models


class AllFacultyUsers(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    department = models.CharField(max_length=255, default='cse')
    mobile_number = models.IntegerField()
    email_address = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)


class FacultyDetails(models.Model):
    ns_id = models.IntegerField()
    employee_id = models.CharField(max_length=20)
    sender_name = models.CharField(max_length=50)


class NoteSheet(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    # date = models.DateTimeField(format='%d-%m-%Y %H:%M', auto_now_add=True)
    subject = models.TextField()
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    objective = models.TextField()
    proposal_details = models.TextField()
    proposal_submitted_by = models.CharField(max_length=255)
    proposal_submitted_by_1 = models.CharField(max_length=255)
    receiver_1 = models.CharField(max_length=255)
    receiver_2 = models.CharField(max_length=255)
    Status = models.IntegerField(default='000')
