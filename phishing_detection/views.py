from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_view(request):
    return Response({"message": "Secure data!"})

def some_view(request):
    return JsonResponse({"message": "Hello from phishing detection!"})
