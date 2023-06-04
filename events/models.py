from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=100, null=False)  # can you set the contents of a charfield using dropdown menus?
    location = models.CharField(max_length=100, null=False)  # does this want to just be text?
    stepfree = models.BooleanField(default=False)
    accessible_toilets = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Performer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    biog = models.TextField()
    photo = models.FileField()
    weblink = models.URLField()

    def __str__(self):
        return self.name


class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    performers = models.ForeignKey(Performer, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name