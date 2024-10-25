from django.shortcuts import render
from core.models import CO2
import plotly.express as px
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When

from core.forms import DateForm
# Create your views here.

def chart(request):
    co2 = CO2.objects.all()

    start = request.GET.get('start')
    end = request.GET.get('end')

    co2_filter = co2
    if start:
        co2_filter = co2.filter(date__gte=start)
    if end:
        co2_filter = co2_filter.filter(date__lte=end)
    
    fig = px.line(
        x = [item.date for item in co2_filter],
        y = [item.average for item in co2_filter],
        title='PLOT',
        labels={'x': 'Date', 'y': 'Average CO2'},
    )

    chart = fig.to_html()
    context= {'chart_plot': chart,
              'form': DateForm(),}

    return render(request, 'core/chart.html', context)

def yearly_avg_co2(request):
    averages = CO2.objects.values('date__year').annotate(avg=Avg('average'))
    x = averages.values_list('date__year', flat=True)
    y = averages.values_list('avg', flat=True)

    fig = px.bar(
        x=x,
        y=y,
    )
    fig.update_layout(
        title='Yearly Average CO2',
        
    )

    bar_chart = fig.to_html()
    context= {
        'bar_chart': bar_chart,
        'form': DateForm(),
    }
    return render(request, 'core/chart.html', context)