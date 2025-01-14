import pytest # type: ignore
from dogs.models import Breed, Dog

@pytest.mark.django_db
def test_breed_creation():
    """
    GIVEN a Breed model
    WHEN a new Breed is created
    THEN check if the breed fields are correct
    """
    breed = Breed.objects.create(
        name="Golden Retriever",
        size="Large",
        friendliness=5,
        trainability=5,
        sheeddingamount=4,
        exerciseneeds=5
    )
    assert breed.name == "Golden Retriever"
    assert breed.size == "Large"
    assert breed.friendliness == 5

@pytest.mark.django_db
def test_dog_creation():
    """
    GIVEN a Dog model
    WHEN a new Dog is created
    THEN check if the dog fields are correct
    """
    breed = Breed.objects.create(name="Labrador", size="Large", friendliness=4, trainability=5, sheeddingamount=3, exerciseneeds=4)
    dog = Dog.objects.create(
        name="Buddy",
        age=3,
        breed=breed,
        gender="Male",
        color="Golden",
        favoritefood="Chicken",
        favoritetoy="Ball"
    )
    assert dog.name == "Buddy"
    assert dog.breed.name == "Labrador"
    assert dog.gender == "Male"
