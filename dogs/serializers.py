from rest_framework import serializers # type: ignore
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        
class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(), source='breeed', write_only=True
    )
    
    class Meta:
        model = Dog
        fields = '__all__'