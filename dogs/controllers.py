import logging
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

# ✅ Configure Logger
logger = logging.getLogger("django")  # Uses Django's logging system

class DogList(APIView):
    def get(self, request):
        logger.info("📌 GET /dogs - Fetching all dogs")
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        logger.info(f"📌 POST /dogs - Creating a new dog with data: {request.data}")
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("✅ New dog created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"⚠️ Validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    def get(self, request, pk):
        logger.info(f"📌 GET /dogs/{pk} - Fetching dog details")
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            logger.error(f"❌ Dog with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        logger.info(f"📌 PUT /dogs/{pk} - Updating dog with data: {request.data}")
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            logger.error(f"❌ Dog with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"✅ Dog with id {pk} updated successfully.")
            return Response(serializer.data)
        logger.warning(f"⚠️ Validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        logger.info(f"📌 DELETE /dogs/{pk} - Deleting dog")
        try:
            dog = Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            logger.error(f"❌ Dog with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        dog.delete()
        logger.info(f"✅ Dog with id {pk} deleted successfully.")
        return Response(status=status.HTTP_204_NO_CONTENT)

class BreedList(APIView):
    def get(self, request):
        logger.info("📌 GET /breeds - Fetching all breeds")
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        logger.info(f"📌 POST /breeds - Creating a new breed with data: {request.data}")
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("✅ New breed created successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"⚠️ Validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreedDetail(APIView):
    def get(self, request, pk):
        logger.info(f"📌 GET /breeds/{pk} - Fetching breed details")
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            logger.error(f"❌ Breed with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk):
        logger.info(f"📌 PUT /breeds/{pk} - Updating breed with data: {request.data}")
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            logger.error(f"❌ Breed with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"✅ Breed with id {pk} updated successfully.")
            return Response(serializer.data)
        logger.warning(f"⚠️ Validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        logger.info(f"📌 DELETE /breeds/{pk} - Deleting breed")
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            logger.error(f"❌ Breed with id {pk} not found.")
            return Response(status=status.HTTP_404_NOT_FOUND)
        breed.delete()
        logger.info(f"✅ Breed with id {pk} deleted successfully.")
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView # type: ignore
# from rest_framework.response import Response # type: ignore
# from rest_framework import status # type: ignore
# from .models import Dog, Breed
# from .serializers import DogSerializer, BreedSerializer

# class DogList(APIView):
#     def get(self, request):
#         dogs = Dog.objects.all()
#         serializer = DogSerializer(dogs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = DogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DogDetail(APIView):
#     def get(self, request, pk):
#         try:
#             dog = Dog.objects.get(pk=pk)
#         except Dog.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = DogSerializer(dog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             dog = Dog.objects.get(pk=pk)
#         except Dog.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = DogSerializer(dog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             dog = Dog.objects.get(pk=pk)
#         except Dog.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         dog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BreedList(APIView):
#     def get(self, request):
#         breeds = Breed.objects.all()
#         serializer = BreedSerializer(breeds, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BreedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BreedDetail(APIView):
#     def get(self, request, pk):
#         try:
#             breed = Breed.objects.get(pk=pk)
#         except Breed.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = BreedSerializer(breed)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             breed = Breed.objects.get(pk=pk)
#         except Breed.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = BreedSerializer(breed, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             breed = Breed.objects.get(pk=pk)
#         except Breed.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         breed.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
