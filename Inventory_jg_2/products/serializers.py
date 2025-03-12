from rest_framework import serializers
from .models import Category
from .models import Item
from datetime import date

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    @staticmethod
    def check_special_caracters(value, field_name):
        special_characters = '!@#$%^&*'
        for char in special_characters:
            if char in value: 
                raise serializers.ValidationError(f"{field_name} cannot contain special characters [!@#$%^&*].")
    
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Name must be at least 5 characters long.")
        self.check_special_caracters(value, 'Name')
        
        return value

    def validate_description(self, value):
        if len(value.split()) < 2:
            raise serializers.ValidationError("Description must have at least 2 words.")
        self.check_special_caracters(value, 'Description')
        return value

    def validate_expiration_date(self, value):
        request = self.context.get('request')
        if value and value < date.today():
            raise serializers.ValidationError("Expiration date cannot be in the past.")
        
        return value

    def validate(self, data):
        # validate dimention fields to be positiove
        numeric_fields = ['width', 'height', 'length', 'weight']
        for field in numeric_fields:
            if data.get(field) and data.get(field) < 0:
                raise serializers.ValidationError({field: f"{field.capitalize()} cannot be negative."})
        
        # validate expiration date to exist for food and drinks 
        if data['category'] and any(word in data['category'].name.lower() for word in ['food', 'drink']) and not data['expiration_date']:
            raise serializers.ValidationError("Expiration date is required for food or drink categories.")
        
        return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


