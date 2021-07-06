from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    id = request.GET.get("id", 1)
    person = Person.objects.get(key=id)
    data = {
        'full_name': person.full_name,
        'date_birth': person.date_birth,
        'expiration_date': person.expiration_date
    }

    return render(request, 'mos/base.html', data)