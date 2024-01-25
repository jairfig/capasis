from django.shortcuts import render


# Create your views here.
def trilhas(request):
    return render(request, 'trilhas.html')
