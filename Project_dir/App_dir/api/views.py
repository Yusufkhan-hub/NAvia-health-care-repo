# Create your views here.
from rest_framework.decorators import api_view
from ..models import primary_model
from .serializers import  test_serializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters


class search_api_view(ListAPIView):
    """
    This is using ListAPIView inbuilt module of DRF which display the list of data or 
    you can filter data by giving sku_name,drug_name or salt_name in a text format
    """
    search_fields = ['sku_name','drug_form','salt_name']
    filter_backends = (filters.SearchFilter,)
    queryset=primary_model.objects.all()
    serializer_class = test_serializer



@api_view(['POST'])
def search_api(request):
    
    """
    This is logic for filter data using api_view decorator. 
    IT has some queries you may run any one of them you want.
    """         
    
    if request.method=="POST":
        data=request.data
        final_data=(data)
        name=final_data['name']
        
    """ This will give each data objects """
    # obj=primary_model.objects.all()
    
    """ This will give data after filtered """
    obj=primary_model.objects.all().filter(sku_name=name)
    
    """ This will give you selected data after filtered """
    # obj=primary_model.objects.values('sku_name','price','salt_name','drug_form','strength').filter(sku_name=name).order_by().distinct()
    
    ser=test_serializer(obj,many=True)
    return Response(ser.data)
    