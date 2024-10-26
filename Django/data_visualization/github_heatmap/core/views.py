from django.shortcuts import render
from .models import *
from .utils import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import plotly.express as px
import calendar
# Create your views here.
@login_required
def commits(request):
    commits = Commit.objects.filter(user=request.user).order_by('created')

    now = timezone.now()
    start = now - timezone.timedelta(weeks=52)
    daterange = date_range(start, now)
    counts = [[] for _ in range(7)]
    dates = [[] for _ in range(7)]
    for dt in daterange:
        count = commits.filter(created__date=dt).count()
        day_number = dt.weekday()
        counts[day_number].append(count)
        dates[day_number].append(dt)

    first_day = daterange[0].weekday()
    dayname = list(calendar.day_name)
    days = dayname[first_day:] + dayname[:first_day]

    fig = px.imshow(
        counts,
        color_continuous_scale='greens',
        x = dates[0],
        y = days,
    )
    fig.update_layout(plot_bgcolor='white')
    fig.update_traces({'xgap': 8, 'ygap': 8})
    chart = fig.to_html()
    context = {
        'chart': chart,
    }
    return render(request, 'commits.html', context)

