from rest_framework import serializers
from products.models import Product
from rest_framework.exceptions import ValidationError

class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    def validate(self,data):
        title = data.get('title')
        if title.isdigit():
            raise ValidationError({'error':'titleda son yozish mumkin ems !'})
        return data

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError({'error': "pricega faqat 0 dan katta bo'lgan son kiriting!"})
        return value

    def validate_description(self, value):
        if len(value) < 20:
            raise ValidationError({'error': "descriptionda  20 ta harf bo'lsin  !"})
        return value




