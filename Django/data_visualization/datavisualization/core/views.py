from django.shortcuts import render
from core.models import CO2
import plotly.express as px

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