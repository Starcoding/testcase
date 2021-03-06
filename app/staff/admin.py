from django.contrib import admin
from .models import Person
from django.utils.html import format_html

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'surname',
        'patronymic',
        'phonenumber',
        'image',
        'preview',
        'date_of_birth',
        'status',
    ]
    search_fields = [
        'first_name',
        'surname',
        'patronymic',
        'phonenumber',
        'date_of_birth',
        'status',
    ]
    readonly_fields = ["preview"]

    def preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;">')
        

