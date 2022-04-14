from django.shortcuts import render, redirect
from .utils import SearchFundings
from .forms import FundingForm, UpdateForm
from django.contrib.auth.decorators import login_required
from .models import Funding, Participant

# Create your views here.

def Fundings(request):
    fundings, search = SearchFundings(request)


    context = {'fundings':fundings, 'search':search}
    return render(request, 'funding/fundings.html', context)

@login_required(login_url="login")
def FundingObj(request, pk):
    object = Funding.objects.get(id=pk)
    profile = request.user.profile
    check = Participant.objects.filter(
        owner = profile,
        funding = object
    )

    count = object.participant_set.count()
    

    if check:
        page = 'exist'
    else:
        Participant.objects.create(owner=profile,funding=object)
        page = 'create'

    if request.method == 'POST':
        object.total_num += object.limitation
        object.save()
        redirect('funding/funding.html')

    context = {'funding':object, 'page':page, 'count':count}

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

