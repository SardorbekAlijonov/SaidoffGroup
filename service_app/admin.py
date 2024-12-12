from django.contrib import admin
from service_app.models import Order, Portfolio, ServiceDescription, Service, Tags
from modeltranslation.admin import TranslationAdmin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service']
    list_display_links = list_display


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id',]


@admin.register(ServiceDescription)
class ServiceDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id',]


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['id',]
    search_fields = [list_display]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id']
