from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from App_dir.models import primary_model
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view
def search_api(request):
    
    if request.method=="POST":
        
        data=request.data
        obj=primary_model.objects.values('sku_name','price','strength','salt_name','drug_form').filter(sku_name=data).order_by().distinct()
        response_data={'data':obj}
        return response_data
        
    