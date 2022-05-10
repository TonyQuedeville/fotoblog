from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Restriction d'accés à la page

@login_required # Restriction d'accés à la page home
def home(request):
    return render(request, 'blog/home.html')

