from rest_framework import serializers # type: ignore
from django.core.validators import EmailValidator
from phonenumbers import parse, is_valid_number
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheeddingamount', 'exerciseneeds']
        
class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)

    class Meta:
        model = Dog
        fields = ['id','name', 'age', 'breed', 'gender','breed_id', 'color', 'favoritefood', 'location', 'favoritetoy', 'email', 'phone_number']
    
    def validate_email(self, value):
        if value:
            email_validator = EmailValidator()
            try:
                email_validator(value)
            except Exception as e:
                raise serializers.ValidationError("Invalid email format.")
        return value
    
    def validate_phone_number(self, value):
        if value:
            try:
                phone_obj = parse(str(value))
                if not is_valid_number(phone_obj):
                    raise serializers.ValidationError("Invalid phone number.")
            except Exception as e:
                raise serializers.ValidationError("Phone number validation error.")
        return value
    