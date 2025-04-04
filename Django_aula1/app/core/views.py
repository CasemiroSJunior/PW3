from django.shortcuts import render
from core.services import verifyHoliday

def natal(request):
    context = {'natal':verifyHoliday('Natal'), 'carnaval':verifyHoliday('Carnaval')}
    print(context)
    return render(request, 'natal.html', context)

