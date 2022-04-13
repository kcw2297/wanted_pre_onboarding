from django.shortcuts import render, redirect
from .utils import SearchFundings
from .forms import FundingForm, UpdateForm
from django.contrib.auth.decorators import login_required
from .models import Funding

# Create your views here.

def Fundings(request):
    fundings, search_query = SearchFundings(request)

    context = {'fundings':fundings, 'search_query':search_query}
    return render(request, 'funding/fundings.html', context)


def FundingObj(request, pk):
    object = Funding.objects.get(id=pk)

    context = {'funding':object}

    return render(request, 'funding/funding.html',context)



@login_required(login_url="login")
def CreateFunding(request):
    profile = request.user.profile
    form = FundingForm()

    if request.method == 'POST':
        form = FundingForm(request.POST, request.FILES)
        if form.is_valid():
            funding = form.save(commit=False)
            funding.owner = profile
            funding.save()
            print(funding)
        return redirect('/')

    context = {'form':form}
    return render(request, 'funding/funding_form.html', context)

@login_required(login_url="login")
def UpdateFunding(request, pk):
    profile = request.user.profile
    funding = profile.funding_set.get(id=pk)
    form = UpdateForm(instance=funding)
    

    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES,instance=funding)
        if form.is_valid():
            funding.save()

        return redirect('/')
    context = {'form':form}
    return render(request, 'funding/funding_form.html', context)

@login_required(login_url="login")
def DeleteFunding(request, pk):
    profile = request.user.profile
    funding = profile.funding_set.get(id=pk)

    if request.method == 'POST':
        funding.delete()
        return redirect('/')
    
    context = {'funding':funding}
    return render(request, 'delete.html',context)



