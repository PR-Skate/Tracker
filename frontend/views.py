from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def storeForm(request):
    return render(request, 'frontend/StoreForm.html')


def workOrderForm(request):
    return render(request, 'frontend/WorkOrderForm.html')


def sowForm(request):
    return render(request, 'frontend/sowForm.html')


def workOrderform(request):
    return render(request, 'frontend/workOrderForm.html')


def customerForm(request):
    return render(request, 'frontend/customerForm.html')
