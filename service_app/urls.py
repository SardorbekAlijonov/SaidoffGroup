from django.urls import path

from service_app.views import ServiceAPIView, ServiceDescriptionAPIView, OrderAPIView, PortfolioListAPIView, \
    TagListAPIView

urlpatterns = [

    path('services/', ServiceAPIView.as_view(), name='service-list'),
    path('service_descriptions/', ServiceDescriptionAPIView.as_view(), name='service-description-list'),
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('portfolios/', PortfolioListAPIView.as_view(), name='portfolio-list'),
    path('tags/', TagListAPIView.as_view(), name='portfolio-list'),

]
