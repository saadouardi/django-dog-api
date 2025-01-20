from django.db import models # type: ignore
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import parse, is_valid_number
from simple_history.models import HistoricalRecords


class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'lARGE'
    SIZE_CHOICES = [
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    ]
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.PositiveSmallIntegerField(default=1)
    trainability = models.PositiveSmallIntegerField(default=1)
    sheeddingamount = models.PositiveSmallIntegerField(default=1)
    exerciseneeds = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name

class Dog(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="dogs")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    favoritetoy = models.CharField(max_length=100)

    # New fields with validation
    email = models.EmailField(
        max_length=254,
        validators=[EmailValidator(message="Invalid email format.")],
        null=True,
    )
    
    phone_number = PhoneNumberField(
        null=True,
        help_text="Enter a valid international phone number (e.g., +1234567890)."
    )
    history = HistoricalRecords()

    # Custom validation for phone number
    def clean_phone_number(self):
        if self.phone_number:
            try:
                phone_obj = parse(str(self.phone_number))
                if not is_valid_number(phone_obj):
                    raise ValueError("Invalid phone number.")
            except Exception as e:
                raise ValueError(f"Phone number validation error: {e}")

    def __str__(self):
        return f"{self.name} ({self.breed.name})"
