from django.shortcuts import render
from core.models import PersonSalary
import plotly.express as px

# Create your views here.
def plot(request):
    person_salaries = PersonSalary.objects.filter(education__in=['1. < HS Grad', '5. Advanced Degree'])
    ages = person_salaries.values_list('age', flat=True)
    salaries = person_salaries.values_list('salary', flat=True)
    color = person_salaries.values_list('education', flat=True)

    fig = px.box(x=ages, y=salaries, title='Salary by Age', height=800)
    html = fig.to_html()

    context = {
        'salaries': person_salaries,
        'chart': html,
    }
    return render(request, 'scatter.html', context)