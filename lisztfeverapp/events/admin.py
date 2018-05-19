from django.contrib import admin
from . import models

# Register your models here.
# @admin.register(models.Event)
# class EventAdmin(admin.ModelAdmin):
#
#     search_fields = ["eventid"]
#     list_display = (
#         "eventid",
#         "eventimageurl",
#         "eventname",
#         "eventstartlocaldate",
#         "eventstatus",
#         "onsaleenddatetime",
#         "onsalestartdatetime",
#         "primaryeventurl",
#         "source",
#         "currency",
#         "maxprice",
#         "minprice",
#         "eventstartlocaltime",
#         "updated_at",
#         "venue"
#     )
#
# @admin.register(models.Venue)
# class VenueAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "venueid",
#         "venuename",
#         "venuecity",
#         "venuestatecode",
#         "venuecountrycode",
#         "venuestreet",
#         "venuezipcode",
#         "venuelatitude",
#         "venuelongitude",
#         "venueurl",
#         "venuetimezone",
#         "updatedat"
#     )
