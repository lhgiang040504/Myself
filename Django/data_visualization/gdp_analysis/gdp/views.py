from django.shortcuts import render
from django.db.models import Max, Min
from .models import GDP
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.embed import components
from bokeh.plotting import figure
# Create your views here.

def index(request):
    min_year = GDP.objects.aggregate(min_year=Min('year'))['min_year']
    max_year = GDP.objects.aggregate(max_year=Max('year'))['max_year']
    year = request.GET.get('year', min_year)

    count = int(request.GET.get('count', 10))

    gdps = GDP.objects.filter(year=year).order_by('gdp').reverse()[:count]

    country_name = [d.country for d in gdps]
    country_gdp = [d.gdp for d in gdps]

    cds = ColumnDataSource(data=dict(country_name=country_name, country_gdp=country_gdp))

    fig = figure(x_range=country_name, height=500, title=f"Top {count} GDPs {year}")
    fig.title.align = 'center'
    fig.title.text_font_size = '1.5em'
    import math
    fig.xaxis.major_label_orientation = math.pi / 4
    fig.yaxis[0].formatter = NumeralTickFormatter(format='$0.0a')


    fig.vbar(x='country_name', top='country_gdp', source=cds, width=0.9, line_color='white', fill_color='skyblue')
    script, div = components(fig)

    context = {
        'script': script,
        'div': div,
        'years': range(min_year, max_year + 1),
        'count': count,
    }
    
    if request.htmx:
        return render(request, 'partials/gdp-bar.html', context)
    return render(request, 'index.html', context)
