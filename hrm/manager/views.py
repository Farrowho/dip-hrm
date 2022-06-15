from django.shortcuts import render, get_object_or_404, redirect
from .models import Applications, Contracts, Departments, \
    DocumentsTypes, EducationType, Log, Orders, \
    Passports, Positions, Workers
from .forms import NewWorkerForm, PassportForm, NewAppForm, NewOrderForm, NewContractForm
from django.http import HttpResponse


def home(request):
    """Рендер главной страницы"""
    departments = Departments.objects.all()
    passports = Passports.objects.all()
    workers = Workers.objects.all()
    return render(request, 'manager/home.html', {'workers': workers,
                                                 'passports': passports,
                                                 'departments': departments})


def new_worker(request):
    """Рендер страницы с формой оформления нового сотрудника (шаг 1)"""
    form = NewWorkerForm()
    if request.method == 'POST':
        form = NewWorkerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_worker.html', context)


def new_worker2(request):
    """Рендер страницы с формой оформления нового сотрудника (шаг 2)"""
    form = PassportForm()
    if request.method == 'POST':
        form = PassportForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_worker_step2.html', context)


def log(request):
    log = Log.objects.all()
    orders = Orders.objects.all()
    applications = Applications.objects.all()
    workers = Workers.objects.all()
    positions = Positions.objects.all()
    documents_types = DocumentsTypes.objects.all()
    context = {'log': log,
               'orders': orders,
               'applications': applications,
               'workers': workers,
               'positions': positions,
               'documents_types': documents_types}
    return render(request, 'manager/log.html', context)


def applications(request):
    applications = Applications.objects.all()
    workers = Workers.objects.all()
    documents_types = DocumentsTypes.objects.all()
    context = {'applications': applications,
               'workers': workers,
               'documents_types': documents_types}
    return render(request, 'manager/applications.html', context)


def worker_detail(request, worker_id):
    """Рендер отдельной страницы проекта"""
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/worker_detail.html', {'workers': workers})


def orders(request):
    orders = Orders.objects.all()
    context = {'orders': orders}
    return render(request, 'manager/orders.html', context)


def contracts(request):
    contracts = Contracts.objects.all()
    context = {'contracts': contracts}
    return render(request, 'manager/contracts.html', context)


def order_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/order_print.html', {'workers': workers})


def new_app(request):
    form = NewAppForm()
    if request.method == 'POST':
        form = NewAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_app.html', context)


def new_order(request):
    form = NewOrderForm()
    if request.method == 'POST':
        form = NewOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_order.html', context)


def new_contract(request):
    form = NewContractForm()
    if request.method == 'POST':
        form = NewContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_contract.html', context)



