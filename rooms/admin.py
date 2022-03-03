from csv import list_dialects
from pyexpat import model
from tkinter import HORIZONTAL
from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item Admin Definition """
    
    list_display = (
        "name",
        "used_by",
    )
    
    def used_by(self, obj):
        return obj.rooms.count()
    
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """
    
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "bath")},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",)
            },
        ),
        ("Last Details", {"fields": ("host",)},),
        
    )
    

    list_display = (
        "name",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
    )

    search_fields = ("^city", "^host__username",)
    
    filter_horizontal = ("amenities", "facilities", "house_rules",)
    
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """ Photo Admin Definition """
    
    pass