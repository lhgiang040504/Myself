from django.shortcuts import render
from core.models import PersonSalary
import plotly.express as px
from django.db.models import Case, When, Value, CharField, Avg

# Create your views here.
def plot(request):
    person_salaries = PersonSalary.objects.filter(education__in=['1. < HS Grad', '5. Advanced Degree'])
    ages = person_salaries.values_list('age', flat=True)
    salaries = person_salaries.values_list('salary', flat=True)

    gaps = 5
    age_bins = [(i, i+gaps-1) for i in range(15, 85, gaps)]
    conditionals = [When(age__range=bin, then=Value(f'{bin}')) for bin in age_bins]

    case = Case(*conditionals, output_field=CharField())
    age_groupings = person_salaries.annotate(age_group=case).values('age_group').order_by('age_group').annotate(avg=Avg('salary'))

    age_groups = age_groupings.values_list('age_group', flat=True)
    salaries = age_groupings.values_list('avg', flat=True)

    fig = px.line(x=age_groups, y=salaries, title='Salary by Age', height=800)
    html = fig.to_html()

    context = {
        'salaries': person_salaries,
        'chart': html,
    }
    return render(request, 'scatter.html', context)