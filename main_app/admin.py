from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main_app.models import Partners, WhyUs, FAQ, FAQ_Category, Feedback, Certificates, Subscriber, Teams


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(WhyUs)
class WhyUAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    search_fields = [list_display]


@admin.register(FAQ)
class FAQAdminAdmin(TranslationAdmin):
    list_display = ['id', 'question']
    search_fields = [list_display]


@admin.register(FAQ_Category)
class FAQCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    search_fields = [list_display]


@admin.register(Feedback)
class FeedbackAdmin(TranslationAdmin):
    list_display =['id', 'name']


@admin.register(Certificates)
class CertificatesAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    search_fields = [list_display]


@admin.register(Teams)
class TeamsAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'profession']
    search_fields = [list_display]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'is_checked']
