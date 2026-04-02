from django.db import models

class Guard(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    rank = models.CharField(max_length=50, choices=[("guard", "Guard"), ("supervisor", "Supervisor"), ("manager", "Manager")], default="guard")
    site = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("on_leave", "On Leave"), ("terminated", "Terminated")], default="active")
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Shift(models.Model):
    guard_name = models.CharField(max_length=255)
    site = models.CharField(max_length=255, blank=True, default="")
    shift_type = models.CharField(max_length=50, choices=[("morning", "Morning"), ("afternoon", "Afternoon"), ("night", "Night")], default="morning")
    date = models.DateField(null=True, blank=True)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("active", "Active"), ("completed", "Completed"), ("absent", "Absent")], default="scheduled")
    hours = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.guard_name

class Incident(models.Model):
    title = models.CharField(max_length=255)
    site = models.CharField(max_length=255, blank=True, default="")
    reported_by = models.CharField(max_length=255, blank=True, default="")
    severity = models.CharField(max_length=50, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High"), ("critical", "Critical")], default="low")
    incident_type = models.CharField(max_length=50, choices=[("theft", "Theft"), ("trespass", "Trespass"), ("fire", "Fire"), ("vandalism", "Vandalism"), ("medical", "Medical"), ("other", "Other")], default="theft")
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("open", "Open"), ("investigating", "Investigating"), ("resolved", "Resolved")], default="open")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
