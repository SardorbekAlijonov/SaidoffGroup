from modeltranslation.translator import register, TranslationOptions
from main_app import models


@register(models.FAQ)
class FAQModel(TranslationOptions):
    fields = ('question', 'answer')


@register(models.WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.FAQ_Category)
class FAQCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment', 'profession')


@register(models.Certificates)
class CertificatesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.Teams)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('profession',)
