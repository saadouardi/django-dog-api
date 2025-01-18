import pytest
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from django.urls import reverse
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer

# Test using Django's test client
@pytest.fixture
def api_client():
    return MagicMock()

# Mock for Breed model creation
@pytest.fixture
def breed_fixture():
    breed = Breed.objects.create(name="Golden Retriever", size=Breed.MEDIUM)
    return breed

# Test Case for Dog Model and Serializer
def test_dog_creation_and_serialization(api_client, breed_fixture):
    # Mock the Dog object creation
    dog_data = {
        "name": "Buddy",
        "age": 3,
        "breed_id": breed_fixture.id,  # Reference the Breed
        "gender": Dog.MALE,
        "color": "Golden",
        "favoritefood": "Chicken",
        "location": "New York",
        "favoritetoy": "Ball",
        "email": "buddy@example.com",
        "phone_number": "+1234567890"
    }
    
    # Call the serializer directly to test validation
    serializer = DogSerializer(data=dog_data)
    assert serializer.is_valid(), f"Serializer errors: {serializer.errors}"

    # Save the object to the database
    dog = serializer.save()

    # Ensure the Dog was created and associated with the Breed correctly
    assert dog.name == "Buddy"
    assert dog.breed.name == "Golden Retriever"
    assert dog.phone_number == "+1234567890"
    
    # Test that the model's clean method works (if you have custom validation)
    dog.clean_phone_number()  # Ensure that the phone number is valid

    # Test via APIClient using the Django REST API
    url = reverse('dog-list')  # Make sure you have a proper URL pattern
    response = api_client.post(url, dog_data, format='json')
    
    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    
    # Validate the response content (use serializer's output)
    response_data = response.json()
    assert response_data['name'] == "Buddy"
    assert response_data['breed'] == breed_fixture.name
    assert response_data['phone_number'] == "+1234567890"

def test_fetch_data(client):
    # Mocking the request and response in Django
    with patch('your_project.views.YourViewClass.fetch_data') as mock_fetch:
        mock_fetch.return_value = {
            'images': ["image1.jpg", "image2.jpg"],
            'total': 2
        }

        # Simulate client request to the endpoint (assuming URL pattern exists)
        response = client.get("/data", params={"searchQuery": "test", "page": 1, "pageSize": 10})
        
        # Then: The response should have a status code of 200
        assert response.status_code == 200
        
        # And: The response should contain a list of images and a total count
        data = response.json()
        assert 'images' in data and isinstance(data['images'], list), "Response does not include an images list"
        assert 'total' in data, "Response does not include a total count"
