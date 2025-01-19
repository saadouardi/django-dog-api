from django.test import TestCase, Client
from django.urls import reverse
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer

class DogModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.breed = Breed.objects.create(name="Golden Retriever", size=Breed.MEDIUM)

    def test_dog_creation_and_serialization(self):
        dog_data = {
            "name": "Buddy",
            "age": 3,
            "breed_id": self.breed.id,  # ✅ Use `breed_id` instead of `breed`
            "gender": Dog.MALE,
            "color": "Golden",
            "favoritefood": "Chicken",
            "location": "New York",
            "favoritetoy": "Ball",
            "email": "buddy@example.com",
            "phone_number": "+14155552671"
        }

        url = reverse('dog-list')  
        response = self.client.post(url, data=dog_data, content_type="application/json")

        self.assertEqual(response.status_code, 201, f"Expected 201 but got {response.status_code}")

        response_data = response.json()
        self.assertEqual(response_data['name'], "Buddy")
        self.assertEqual(response_data['breed']['name'], "Golden Retriever")  
        self.assertEqual(response_data['phone_number'], "+14155552671")

class FetchDataTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_fetch_data(self):
        url = reverse("dog-list")
        response = self.client.get(url, content_type="application/json")
        self.assertEqual(response.status_code, 200, f"Expected 200 but got {response.status_code}")

        data = response.json()
        if isinstance(data, list):
            self.assertIsInstance(data, list, "Response should be a list")
        else:
            self.assertIn('results', data, "Response does not include a 'results' key")
            self.assertIsInstance(data['results'], list, "Results should be a list")
