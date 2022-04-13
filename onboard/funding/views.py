from django.shortcuts import render, redirect


# Create your views here.

def fundings(request):
    return render(request, 'funding/fundings.html')



def registerFunding(request):
    return render(request, 'funding/funding_form.html')


def viewDetail(request):
    return render(request, 'funding/detail.html')
