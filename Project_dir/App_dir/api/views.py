from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from ..models import primary_model


@api_view
def search_api(request):
    
    if request.method=="POST":
        
        data=request.data
        obj=primary_model.objects.values('sku_name','price','strength','salt_name','drug_form').filter(sku_name=data).order_by().distinct()
        response_data={'data':obj}
        return response_data
        
    
    