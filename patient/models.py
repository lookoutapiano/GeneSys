from django.db import models
from django.utils import timezone


class Patient (models.Model):
    PatientID = models.AutoField(primary_key=True)
    GivenName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Extention = models.CharField(max_length=5, null=True)
    DOB = models.DateField()
    Gender = models.CharField(max_length=12)
    StreetAdd = models.CharField(max_length=255)
    BrgyAdd = models.CharField(max_length=255)
    CityAdd = models.CharField(max_length=255)
    Region = models.CharField(max_length=27)
    ContactPerson = models.CharField(max_length=50)
    ContactNumber = models.IntegerField()
    DateCreated = models.DateTimeField(default=timezone.now)
    #CreatedBy = models.ForeignKey(User,)
    def __str__(self):
        return self.GivenName
