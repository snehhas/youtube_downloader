from django.shortcuts import redirect, render
from django.http import HttpResponse, request
import django.http.request
# from .forms import ItemForm
from .models import Item
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request, 'sort/home.html')
        

    if request.method =='POST':
        inputval=request.POST['val']
        try:
            val = int(inputval)
            return render(request,'sort/result.html',{'number':inputval})
        except ValueError:
            if inputval.isalpha():
                return render(request,'sort/result.html',{'letter':inputval})
            elif inputval.isalnum():
                return render(request,'sort/result.html',{'letterwithnum':inputval})
        return HttpResponse("Invalid Input")
                

        return render(request, 'sort/result.html',{'number':inputval})

def sort(request):
    if request.method == "GET":
        f = Item()
        return render(request,'sort/result.html')

    f = Item(request.POST)
    if f.is_valid():
        f.save()
        messages.success(request, 'Data Saved')
        return redirect('home')
    return HttpResponse("Success")
        