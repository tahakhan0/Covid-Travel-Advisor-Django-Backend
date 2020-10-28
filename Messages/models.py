from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.postgres.fields import ArrayField


class Country(models.Model):
    name = models.TextField(max_length=20)
    country_code = models.TextField(max_length=4)

    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.name


class APIs(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "APIs"

    def __str__(self):
        return self.name


# class bulkMessages(models.Model):
#     text = models.CharField(max_length=100, null=True, blank=True)

#     class Meta:
#         verbose_name_plural = "Bulk Messages"


class Content(models.Model):
    contents = models.CharField(max_length=140)


class MessagesFromAPI(models.Model):

    COVID_TEST_CHOICES = [
        ('Yes', "Yes"),
        ("No", "No"),
        ("N/A", "N/A")
    ]
    country = models.ForeignKey(
        Country, blank=True, null=True, related_name='messages_country_code', on_delete=models.CASCADE)
    api = models.ManyToManyField(APIs, blank=True)
    restricted_countries = models.ManyToManyField(
        Country, blank=True, related_name="restricted_countries")
    confirmed = models.PositiveIntegerField(default=0, null=True, blank=True)
    deaths = models.PositiveIntegerField(default=0, null=True, blank=True)
    recovered = models.PositiveIntegerField(default=0, null=True, blank=True)
    content = ArrayField(models.TextField(max_length=2000, blank=True))
    # content = models.ManyToManyField(Content, blank=True)

    test_required = models.CharField(
        max_length=3, choices=COVID_TEST_CHOICES, default='No')
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # messages = models.ManyToManyField(bulkMessages, blank=True)

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.country.name

    @property
    def get_last_updated_date(self):
        return self.last_updated.strftime("%m/%d/%Y,%H:%M")

