from .models import Funding
from django.db.models import Q



def SearchFundings(request):
    search_query = ''

    if request.GET.get('search'):
        search_query = request.GET.get('search')
        print(search_query)
    
    fundings = Funding.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return fundings, search_query

def Sorting(request, fundings):
    sort = ''

    if request.GET.get('order_by'):
        sort = request.GET.get('order_by')

        if sort == '생성일':
            fundings = fundings.order_by('-created')
        elif sort == '총펀딩금액':
            fundings = fundings.order_by('-total_num')

    return fundings