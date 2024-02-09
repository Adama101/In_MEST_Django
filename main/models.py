from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import Cohort
from users.models import IMUser


class Title(AbstractUser):
    TITLES = (
        ('MISTER', 'Mr'),
        ('MISSIS', 'Mrs'),
        ('MISS', 'Ms')
    )
class Organiser():
    ORGANISER =(
        ('BRIGHT', 'Bright'),
        ('AFI', 'Afi'),
        ('LUCKY', 'Lucky'),
        ('LADY O', 'Lady O')
        ('EMILY', 'Emily')
    )
class Venue():
    VENUE =(
        ('GL ROOM 1', 'Guest Lecture Room 1')
        ('GL ROOM 2', 'Guest Lecture Room 2')
        ('GL ROOM 3', 'Guest Lecture Room 3')
        ('INCUBATOR', 'MINC Guest Lecture Room')
    )
class resolution():
    RESOLUTION = (
        ('PENDING,', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Decline'),
        ('RESOLVED', 'Resolved')
    )


class ClassSchedule(models.Model):
    title = models.ForeignKey(Title),
    description = models.CharField(max_length=100),
    start_date_and_time = models.DateTimeField(),
    end_date_and_time = models.DateTimeField(),
    is_repeated = models.BooleanField(default = False),
    is_active = models.CharField(max_length= 10, blank= True),
    organizer = models.ForeignKey(choices = Organiser),
    cohort = models.ForeignKey(Cohort)
    venue = models.ForeignKey(choices = Venue)
    # We can also use: 
    # "venue = models.CharField(max_length=100)"
    
    def __str__(self) -> str:
        return self.title

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule),
    attendee = models.ForeignKey(IMUser),
    is_present = models.BooleanField(default = True),
    date_created = models.DateTimeField(),
    author = models.ForeignKey(IMUser)
    
    def __str__(self) -> str:
        return f"{self.attendee} - {self.class_schedule}"

class Query():
    title = models.ForeignKey(Title)
    description = models.TextField(max_length = 100)
    submitted_by = models.ForeignKey(IMUser),
    assigned_to = models.ForeignKey(IMUser),
    resolution_status = models.ForeignKey(max_length = 10, choices = resolution ),
    date_created = models.DateTimeField(),
    date_modified = models.DateTimeField(),
    author = models.ForeignKey(IMUser)
    
    def __str__(self) -> str:
        return self.title

class QueryComment():
    query = models.ForeignKey(Query),
    comment = models.TextField(max_length = 100),
    date_created = models.DateTimeField(auto_now_add = True),
    date_modified = models.DateTimeField(auto_now = True),
    author = models.ForeignKey(IMUser)
    
    def __str__(self):
        return f"comment on: {self.query.title}"
    
