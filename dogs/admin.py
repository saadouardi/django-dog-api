from django.contrib import admin # type: ignore
from simple_history.admin import SimpleHistoryAdmin
from .models import Dog, Breed

# admin.site.register(Dog)
admin.site.register(Breed)

@admin.register(Dog)
class DogAdmin(SimpleHistoryAdmin):
    pass