from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('edit_expense/<int:id>', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:id>', views.delete_expense, name="delete_expense"),
]