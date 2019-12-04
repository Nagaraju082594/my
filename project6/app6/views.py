from django.shortcuts import render
def showmain(request):
    employee_details={
        "101":{"name":"ranjith","salary":185000.00},
        "102":{"name":"nagaraju","salary":10000.00},
        "103":{"name":"rakesh","salary":20000.00}
    }
    return render(request,"index.html",{"data":employee_details})

# Create your views here.
