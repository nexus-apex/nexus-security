import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Guard, Shift, Incident


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['guard_count'] = Guard.objects.count()
    ctx['guard_guard'] = Guard.objects.filter(rank='guard').count()
    ctx['guard_supervisor'] = Guard.objects.filter(rank='supervisor').count()
    ctx['guard_manager'] = Guard.objects.filter(rank='manager').count()
    ctx['shift_count'] = Shift.objects.count()
    ctx['shift_morning'] = Shift.objects.filter(shift_type='morning').count()
    ctx['shift_afternoon'] = Shift.objects.filter(shift_type='afternoon').count()
    ctx['shift_night'] = Shift.objects.filter(shift_type='night').count()
    ctx['shift_total_hours'] = Shift.objects.aggregate(t=Sum('hours'))['t'] or 0
    ctx['incident_count'] = Incident.objects.count()
    ctx['incident_low'] = Incident.objects.filter(severity='low').count()
    ctx['incident_medium'] = Incident.objects.filter(severity='medium').count()
    ctx['incident_high'] = Incident.objects.filter(severity='high').count()
    ctx['recent'] = Guard.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def guard_list(request):
    qs = Guard.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(rank=status_filter)
    return render(request, 'guard_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def guard_create(request):
    if request.method == 'POST':
        obj = Guard()
        obj.name = request.POST.get('name', '')
        obj.employee_id = request.POST.get('employee_id', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.rank = request.POST.get('rank', '')
        obj.site = request.POST.get('site', '')
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/guards/')
    return render(request, 'guard_form.html', {'editing': False})


@login_required
def guard_edit(request, pk):
    obj = get_object_or_404(Guard, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.employee_id = request.POST.get('employee_id', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.rank = request.POST.get('rank', '')
        obj.site = request.POST.get('site', '')
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/guards/')
    return render(request, 'guard_form.html', {'record': obj, 'editing': True})


@login_required
def guard_delete(request, pk):
    obj = get_object_or_404(Guard, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/guards/')


@login_required
def shift_list(request):
    qs = Shift.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(guard_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(shift_type=status_filter)
    return render(request, 'shift_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def shift_create(request):
    if request.method == 'POST':
        obj = Shift()
        obj.guard_name = request.POST.get('guard_name', '')
        obj.site = request.POST.get('site', '')
        obj.shift_type = request.POST.get('shift_type', '')
        obj.date = request.POST.get('date') or None
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.status = request.POST.get('status', '')
        obj.hours = request.POST.get('hours') or 0
        obj.save()
        return redirect('/shifts/')
    return render(request, 'shift_form.html', {'editing': False})


@login_required
def shift_edit(request, pk):
    obj = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        obj.guard_name = request.POST.get('guard_name', '')
        obj.site = request.POST.get('site', '')
        obj.shift_type = request.POST.get('shift_type', '')
        obj.date = request.POST.get('date') or None
        obj.check_in = request.POST.get('check_in') or None
        obj.check_out = request.POST.get('check_out') or None
        obj.status = request.POST.get('status', '')
        obj.hours = request.POST.get('hours') or 0
        obj.save()
        return redirect('/shifts/')
    return render(request, 'shift_form.html', {'record': obj, 'editing': True})


@login_required
def shift_delete(request, pk):
    obj = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/shifts/')


@login_required
def incident_list(request):
    qs = Incident.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(severity=status_filter)
    return render(request, 'incident_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def incident_create(request):
    if request.method == 'POST':
        obj = Incident()
        obj.title = request.POST.get('title', '')
        obj.site = request.POST.get('site', '')
        obj.reported_by = request.POST.get('reported_by', '')
        obj.severity = request.POST.get('severity', '')
        obj.incident_type = request.POST.get('incident_type', '')
        obj.date = request.POST.get('date') or None
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/incidents/')
    return render(request, 'incident_form.html', {'editing': False})


@login_required
def incident_edit(request, pk):
    obj = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.site = request.POST.get('site', '')
        obj.reported_by = request.POST.get('reported_by', '')
        obj.severity = request.POST.get('severity', '')
        obj.incident_type = request.POST.get('incident_type', '')
        obj.date = request.POST.get('date') or None
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/incidents/')
    return render(request, 'incident_form.html', {'record': obj, 'editing': True})


@login_required
def incident_delete(request, pk):
    obj = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/incidents/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['guard_count'] = Guard.objects.count()
    data['shift_count'] = Shift.objects.count()
    data['incident_count'] = Incident.objects.count()
    return JsonResponse(data)
