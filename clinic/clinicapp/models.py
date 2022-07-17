from django.db import models

# Create your models here.
class WorkTimes(models.Model):
    day = models.CharField(max_length=300)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.day


class OnlineWorkTimes(models.Model):
    day = models.CharField(max_length=300)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.day


class Location(models.Model):
    address = models.CharField(max_length=300)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)

    def __str__(self):
        return self.address


class Contact(models.Model):
    email = models.CharField(max_length=300)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=300)
    whatsapp = models.CharField(max_length=300)


class Terms(models.Model):
    title = models.CharField(max_length=50)
    terms = models.TextField()

    def __str__(self):
        return self.title
