from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('guards/', views.guard_list, name='guard_list'),
    path('guards/create/', views.guard_create, name='guard_create'),
    path('guards/<int:pk>/edit/', views.guard_edit, name='guard_edit'),
    path('guards/<int:pk>/delete/', views.guard_delete, name='guard_delete'),
    path('shifts/', views.shift_list, name='shift_list'),
    path('shifts/create/', views.shift_create, name='shift_create'),
    path('shifts/<int:pk>/edit/', views.shift_edit, name='shift_edit'),
    path('shifts/<int:pk>/delete/', views.shift_delete, name='shift_delete'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('incidents/create/', views.incident_create, name='incident_create'),
    path('incidents/<int:pk>/edit/', views.incident_edit, name='incident_edit'),
    path('incidents/<int:pk>/delete/', views.incident_delete, name='incident_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
