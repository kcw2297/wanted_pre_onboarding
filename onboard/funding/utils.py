from .models import Funding, Participant
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def SearchFundings(request):
    search_query = ''

    if request.GET.get('search_funding'):
        search_query = request.GET.get('search_funding')
    
    fundings = Funding.objects.distinct().filter(
        Q(owner__name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(title__icontains=search_query)
    )

    return fundings, search_query