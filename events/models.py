from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    stepfree = models.BooleanField(default=False)
    accessible_toilets = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']


class Performer(models.Model):
    name = models.CharField(max_length=100)
    biog = models.TextField(null=True, blank=True)
    photo = models.FileField(null=True, blank=True)
    weblink = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']

class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    type = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    performers = models.ManyToManyField(Performer)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['date','start_time', 'venue__name']