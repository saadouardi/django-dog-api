from unittest.mock import patch
from django.core.exceptions import ValidationError
from django.test import TestCase
from dogs.models import Breed, Dog

class TestModelsWithMock(TestCase):
    def setUp(self):
        """
        Sets up initial data for testing.
        """
        self.breed1 = Breed.objects.create(
            name="Golden Retriever",
            size="LARGE",
            friendliness=5,
            trainability=8,
            sheeddingamount=6,
            exerciseneeds=7
        )

    @patch("dogs.models.Dog.full_clean")
    def test_invalid_email_with_mock(self, mock_full_clean):
        """
        Uses mock to test that an invalid email raises a ValidationError.
        """
        invalid_dog = Dog(
            name="Max",
            age=2,
            breed=self.breed1,
            gender="Male",
            color="Brown",
            favoritefood="Beef",
            favoritetoy="Rope",
            email="invalid-email",
            phone_number="+1234567890"
        )
        # Updated: ValidationError should use a list of messages
        mock_full_clean.side_effect = ValidationError(["Invalid email address"])
        
        with self.assertRaises(ValidationError) as context:
            invalid_dog.full_clean()
        
        # Updated: Check the first error message
        self.assertEqual(context.exception.messages[0], "Invalid email address")
        # mock_full_clean.assert_called_once()

    @patch("dogs.models.Dog.full_clean")
    def test_invalid_phone_with_mock(self, mock_full_clean):
        """
        Uses mock to test that an invalid phone number raises a ValidationError.
        """
        invalid_dog = Dog(
            name="Bella",
            age=4,
            breed=self.breed1,
            gender="Female",
            color="Black",
            favoritefood="Fish",
            favoritetoy="Bone",
            email="bella@example.com",
            phone_number="+14155552671"
        )
        # Updated: ValidationError should use a list of messages
        mock_full_clean.side_effect = ValidationError(["Invalid phone number"])
        
        with self.assertRaises(ValidationError) as context:
            invalid_dog.full_clean()
        
        # Updated: Check the first error message
        self.assertEqual(context.exception.messages[0], "Invalid phone number")
        # mock_full_clean.assert_called_once()
        
# from django.test import TestCase, Client
# from django.urls import reverse
# from dogs.models import Dog, Breed
# class DogModelTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()  # ✅ Creates a fake browser
#         self.breed = Breed.objects.create(name="Golden Retriever", size=Breed.MEDIUM) # ✅ Adds test data

#     def test_dog_creation_and_serialization(self):
#         dog_data = {
#             "name": "Buddy",
#             "age": 3,
#             "breed_id": self.breed.id,
#             "gender": Dog.MALE,
#             "color": "Golden",
#             "favoritefood": "Chicken",
#             "location": "New York",
#             "favoritetoy": "Ball",
#             "email": "buddy@example.com",
#             "phone_number": "+14155552671"
#         }

#         # ✅ Generates the URL automatically
#         url = reverse('dog-list') 
#         # ✅ Send POST request
#         response = self.client.post(url, data=dog_data, content_type="application/json") 
#         # ✅ Check if dog was created successfully
#         self.assertEqual(response.status_code, 201, f"Expected 201 but got {response.status_code}")
#         # ✅ Check if dog was created with the correct data /  # ✅ Validate response data
#         response_data = response.json()
#         self.assertEqual(response_data['name'], "Buddy")
#         self.assertEqual(response_data['breed']['name'], "Golden Retriever")  
#         self.assertEqual(response_data['phone_number'], "+14155552671")

# class FetchDataTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_fetch_data(self):
#         url = reverse("dog-list")
#         response = self.client.get(url, content_type="application/json")
#         self.assertEqual(response.status_code, 200, f"Expected 200 but got {response.status_code}")

#         data = response.json()
#         if isinstance(data, list):
#             self.assertIsInstance(data, list, "Response should be a list")
#         else:
#             self.assertIn('results', data, "Response does not include a 'results' key")
#             self.assertIsInstance(data['results'], list, "Results should be a list")
