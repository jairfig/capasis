from django.shortcuts import render

# Create your views here.
def trilha(request):
    return render(request, 'trilha.html')
