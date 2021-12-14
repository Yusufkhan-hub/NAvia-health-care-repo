from django.shortcuts import redirect, render
from .models import primary_model
import logging
# Create your views here.

"""Home page"""
def home(request):
    return render(request,'home.html')

"""This is POST logic for manully fitering the data."""
def result(request):
    if request.method=="POST":
        try:
            name=request.POST['medic_name']
            obj=primary_model.objects.values('sku_name','price','strength','salt_name','drug_form').filter(sku_name=name).order_by().distinct()
            if len(obj)==0:
                logging.info("Data not found with selected name")
                return render(request,'data_not_found.html')
            else:    
                logging.info("Data found with selected name")            
                context = {'Medic':obj}
                return render(request,'search-result.html',context)
        except:
            return redirect('home')
    else:        
        return redirect('home')