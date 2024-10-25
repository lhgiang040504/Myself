
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart, name='chart_plot'),
    path('bar_chart', views.yearly_avg_co2, name='bar_chart')
]
