from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class DogList(APIView):
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    def get(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):
    def get(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreedDetail(APIView):
    def get(self, request, pk):
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
