from django.shortcuts import render, redirect

# translate
from django.utils.translation import activate
# Create your views here.

def reserve_view(request):
    return render(request, "reservations/index.html")


def change_lang(request):
    activate('fa')
    return redirect('/reservation/')