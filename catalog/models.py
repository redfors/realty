from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse

from profiles.models import Profile


# Create your models here.

class StatusesRealty(models.Model):
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """status"""
        verbose_name_plural = """statuses"""




class Realty(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField("Name", max_length=150)
    url = models.SlugField(max_length=250, unique=True)
    overview = models.CharField("Overview", max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    description = models.TextField("Description")
    description_data = models.TextField("Description data")
    description_details = models.TextField("Detailed description")
    place = models.TextField("Object location")
    # google_map_data = JSONField("Data location", null=True)
    lat = models.FloatField("Latitude", max_length=50)
    long = models.FloatField("Longitude", max_length=50)
    code = models.CharField("Code", max_length=50)
    type = models.CharField("Type", max_length=255)
    area = models.IntegerField("Area")
    floor_number = models.IntegerField("Floor number")
    namber_of_floors = models.IntegerField("Namber of floors")
    price = models.IntegerField("Price")
    buiding = models.IntegerField("Buiding")
    adaptation = models.IntegerField("Adaptation")
    rooms = models.IntegerField("Rooms")
    garage = models.BooleanField("Garage")
    pool = models.BooleanField("Pool")
    furniture = models.BooleanField("Furniture")
    air_conditioner = models.BooleanField("Air conditioner")

    status_realty = models.ForeignKey(StatusesRealty, on_delete=models.CASCADE, verbose_name="Status realty",
                                      blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User", blank=True, null=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delited = models.DateTimeField(auto_now=True)

    published = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('realty_details', kwargs={'slug': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = """object"""
        verbose_name_plural = """objects"""


class Images(models.Model):
    name = models.CharField("Name", max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    photos = models.ForeignKey(Realty, on_delete=models.CASCADE, verbose_name="Photos", blank=True, null=True)

    def __str__(self):
        return self.name