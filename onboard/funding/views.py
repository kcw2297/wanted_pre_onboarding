from django.shortcuts import render


# Create your views here.

def fundings(request):
    return render(request, 'funding/fundings.html')