import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    app_id = "89d577175eda04c2b91668701e40fa1f"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + app_id

    citys = City.objects.all()

    all_citys = []

    for city in citys:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': round(res['main']['temp'], 1),
            'icon': res['weather'][0]['icon']
        }

        all_citys.append(city_info)

    context = {
        'all_info': all_citys,
        'form': form
    }

    return render(request, 'weather/index.html', context)


# Create your views here.
def about(request):
    return render(request, 'weather/index.html')
