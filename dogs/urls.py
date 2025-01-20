from django.contrib import admin  # type: ignore
from django.urls import include, path # type: ignore
from .controllers import DogList, DogDetail, BreedList, BreedDetail
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dogs/', DogList.as_view(), name="dog-list"),
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]