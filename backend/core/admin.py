from django.contrib import admin
from .models import Guard, Shift, Incident

@admin.register(Guard)
class GuardAdmin(admin.ModelAdmin):
    list_display = ["name", "employee_id", "phone", "email", "rank", "created_at"]
    list_filter = ["rank", "status"]
    search_fields = ["name", "employee_id", "phone"]

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ["guard_name", "site", "shift_type", "date", "check_in", "created_at"]
    list_filter = ["shift_type", "status"]
    search_fields = ["guard_name", "site"]

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ["title", "site", "reported_by", "severity", "incident_type", "created_at"]
    list_filter = ["severity", "incident_type", "status"]
    search_fields = ["title", "site", "reported_by"]
