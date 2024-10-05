from rest_framework import serializers
from .models import WhyUs, Partners, Teams, Certificates, FAQ, Feedback, FAQ_Category, Subscriber


class WhyusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id']


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FAQCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ_Category
        fields = ['id']


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
