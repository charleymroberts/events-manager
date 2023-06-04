from django.db import models

# Create your models here.


class Event(models.Model):
    date = models.DateField()  # do these need parameters?
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # what else goes here? ondelete?
    name = models.CharField(max_length=100, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)  # null vs false?
    performers = models.ForeignKey(Performer, on_delete=models.CASCADE)  # ondelete?
    published = models.BooleanField(default=False)


class Venue(models.Model):
    name = models.CharField(null=False)  # can you set the contents of a charfield using dropdown menus?
    location = models.CharField(null=False)  # does this want to just be text?
    stepfree = models.BooleanField(default=False)
    accessible_toilets = models.BooleanField(default=False)


class Performer(models.Model):
    name = models.CharField(null=False, blank=False)
    biog = models.TextField()
    photo = models.ImageField()
    weblink = models.URLField()
