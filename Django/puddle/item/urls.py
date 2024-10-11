"""
urlpatterns = [
    path('<int:pk>/', views.detail, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
"""
from django.urls import path, include
from . import views  # Import views from your products app

app_name = 'item'  # Optional namespace (explained later)

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    # ... other URL patterns for your products app ...
]