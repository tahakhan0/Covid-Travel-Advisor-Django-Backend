from django.contrib import admin
from Messages.models import *
# Register your models here.
admin.site.register(Country)


@admin.register(MessagesFromAPI)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('country', 'confirmed', 'recovered',
                    'test_required', 'last_updated')


@admin.register(APIs)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
