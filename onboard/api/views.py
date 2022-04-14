from rest_framework.decorators import api_view
from rest_framework.response import Response
from funding.models import Funding
from .serializers import FundingSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects/id'},
        {'GET': '/api/fundings'},
        {'GET': '/api/funding/id'},
    ]

    return Response(routes)


@api_view(['GET'])
def getFundings(request):
    fundings = Funding.objects.all()
    serializer = FundingSerializer(fundings, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getFunding(request, pk):
    funding = Funding.objects.get(id=pk)
    serializer = FundingSerializer(funding, many=False)

    return Response(serializer.data)