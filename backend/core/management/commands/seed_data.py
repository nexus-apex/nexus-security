from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Guard, Shift, Incident
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSecurity with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexussecurity.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Guard.objects.count() == 0:
            for i in range(10):
                Guard.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    employee_id=f"Sample {i+1}",
                    phone=f"+91-98765{43210+i}",
                    email=f"demo{i+1}@example.com",
                    rank=random.choice(["guard", "supervisor", "manager"]),
                    site=f"Sample {i+1}",
                    status=random.choice(["active", "on_leave", "terminated"]),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Guard records created'))

        if Shift.objects.count() == 0:
            for i in range(10):
                Shift.objects.create(
                    guard_name=f"Sample Shift {i+1}",
                    site=f"Sample {i+1}",
                    shift_type=random.choice(["morning", "afternoon", "night"]),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    check_in=date.today() - timedelta(days=random.randint(0, 90)),
                    check_out=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["scheduled", "active", "completed", "absent"]),
                    hours=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 Shift records created'))

        if Incident.objects.count() == 0:
            for i in range(10):
                Incident.objects.create(
                    title=f"Sample Incident {i+1}",
                    site=f"Sample {i+1}",
                    reported_by=f"Sample {i+1}",
                    severity=random.choice(["low", "medium", "high", "critical"]),
                    incident_type=random.choice(["theft", "trespass", "fire", "vandalism", "medical", "other"]),
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["open", "investigating", "resolved"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Incident records created'))
