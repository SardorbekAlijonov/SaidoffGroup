from packaging.tags import Tag
from rest_framework import serializers
from .models import Service, ServiceDescription, Order, Portfolio, Tags


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDescription
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'name',
            'phone_number',
            'message',
            'service',
        ]
    extra_kwargs = {
        'message': {'allow_null': True, 'allow_blank': True}
    }

    def create(self, validated_data):
        order = Order.objects.create(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            message=validated_data['message'],
            service=validated_data['service']
        )
        return order


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
