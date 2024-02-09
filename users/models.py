from django.db import models
from django.contrib.auth.models import AbstractUser

class IMUser(AbstractUser):
    USER_TYPES = (
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin'),
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username


class Cohort(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member} - {self.cohort}"