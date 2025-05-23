from django.contrib import admin
from .models import *

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model']
    list_select_related = ['brand', 'model']

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(FuelConsumption)
class FuelConsumptionAdmin(admin.ModelAdmin):
    list_display = ['city_consumption', 'highway_consumption', 'mixed_consumption']

@admin.register(DriveType)
class DriveTypeAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(TransmissionType)
class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ['transport_type', 'brand_model', 'year', 'body_type', 'fuel_type', 'engine_volume', 'engine_power', 'fuel_consumption', 'drive_type', 'transmission_type', 'color', 'mileage', 'owners_number']
    list_select_related = ['transport_type', 'brand_model', 'body_type', 'fuel_type', 'fuel_consumption', 'drive_type', 'transmission_type', 'color']

@admin.register(TransportPhoto)
class TransportPhotoAdmin(admin.ModelAdmin):
    list_display = ['transport', 'image']
    list_select_related = ['transport']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_dispay = ['value']
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['value']

@admin.register(RegionCity)
class RegionCityAdmin(admin.ModelAdmin):
    list_display = ['region', 'city']
    list_select_related = ['region', 'city']

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['user', 'transport', 'slug', 'price', 'region_city', 'description', 'created', 'updated']
    list_select_related = ['user', 'transport', 'region_city']
    
@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user','advert']
    list_select_related = ['user', 'advert']