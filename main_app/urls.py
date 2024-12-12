from django.urls import path
from main_app import views

urlpatterns = [
    path('whyus/', views.WhyusListAPIView.as_view(), name='whyus-list'),
    path('partners/', views.PartnersListAPIView.as_view(), name='partners-list'),

    path('teams/', views.TeamsListAPIView.as_view(), name='teams-detail'),

    path('certificates/', views.CertificatesListAPIView.as_view(), name='certificates-list'),

    path('faq-categories/', views.FAQCategoryListAPIView.as_view(), name='faqcategory-list-create'),

    path('faqs/', views.FAQListAPIView.as_view(), name='faq-detail'),

    path('feedback/', views.FeedbackListAPIView.as_view(), name='feedback-list'),

    path('subscribers/', views.SubscriberListAPIView.as_view(), name='subscriber-detail'),
]
