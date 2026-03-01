from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'surname',
        'first_name',
        'gender',
        'vocational_skill',
        'status',
        'submitted_at',
    )

    list_filter = (
        'status',
        'gender',
        'vocational_skill',
        'submitted_at',
    )

    search_fields = (
        'surname',
        'first_name',
        'guardian_name',
        'guardian_phone',
    )

    ordering = ('-submitted_at',)