from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from profiles.models import Profile
from django_google_maps import fields as map_fields


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
    address = map_fields.AddressField(max_length=200, default='Любляна')
    geolocation = map_fields.GeoLocationField(max_length=100, default='46.05187370933915,14.506043267333983')
    code = models.CharField("Code", max_length=50)
    type = models.CharField("Type", max_length=255)
    area = models.CharField("Area", max_length=255)
    floor_number = models.CharField("Floor number", max_length=255)
    namber_of_floors = models.CharField("Namber of floors", max_length=255)
    price = models.CharField("Price", max_length=255)
    buiding = models.CharField("Buiding", max_length=255)
    adaptation = models.CharField("Adaptation", max_length=255)
    rooms = models.CharField("Rooms", max_length=255)
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
