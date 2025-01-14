from django.contrib import admin # type: ignore
from .models import Dog, Breed

admin.site.register(Dog)
admin.site.register(Breed)
