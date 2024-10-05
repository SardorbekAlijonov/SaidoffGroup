from modeltranslation.translator import register, TranslationOptions
from service_app import models

@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)
