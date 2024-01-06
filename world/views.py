from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from world.models import Country


def home(request):
    return render(request,'a.html')

def index(request):
    query = request.GET.get('q')
    countries = Country.objects.all()

    if query:
        countries = countries.filter(Q(name__icontains=query) | Q(sov_a3__icontains=query))

    # Organize countries into a dictionary based on the initial letter
    countries_by_letter = {}
    for country in countries:
        initial_letter = country.name[0].upper()
        countries_by_letter.setdefault(initial_letter, []).append(country)

    context = {'countries_by_letter': countries_by_letter, 'query': query}
    return render(request, 'index.html', context)

def country(request, iso_code):
    country = get_object_or_404(Country, sov_a3=iso_code)
    context = {'country': country}
    return render(request, 'country.html', context)
