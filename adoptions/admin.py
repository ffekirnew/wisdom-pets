from django.contrib import admin
from .models import Pet, Vaccine


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'age', 'sex', 'breed']

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass
