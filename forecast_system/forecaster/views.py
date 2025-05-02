from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def root_view(request):
    return Response({"message": "Forecasting Service API"}, status=status.HTTP_200_OK)

