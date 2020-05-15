from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def customerForm(request):
    return render(request, 'frontend/customerForm.html')

def employeeForm(request):
    return render(request, 'frontend/employeeForm.html')

def prepWorkForm(request):
    return render(request, 'frontend/prepWorkForm.html')

def sowForm(request):
    return render(request, 'frontend/sowForm.html')

def storeForm(request):
    return render(request, 'frontend/storeForm.html')

def workOrderForm(request):
    return render(request, 'frontend/workOrderForm.html')


