from django.db import models # type: ignore

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
    favoritetoy = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} ({self.breed.name})"