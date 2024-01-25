from django.shortcuts import render

# Create your views here.
def professor(request):
    return render(request, 'professor.html')