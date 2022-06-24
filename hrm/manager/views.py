from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Applications, Contracts, Departments, Orders, Passports, Workers
from .forms import NewWorkerForm, PassportForm, NewAppForm, NewOrderForm, NewContractForm


def home(request):
    departments = Departments.objects.all()
    passports = Passports.objects.all()
    workers = Workers.objects.all()
    return render(request, 'manager/home.html', {'workers': workers,
                                                 'passports': passports,
                                                 'departments': departments})


def new_worker(request):
    form = NewWorkerForm()
    if request.method == 'POST':
        form = NewWorkerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_worker.html', context)


def edit_worker(request, worker_id):
    worker = get_object_or_404(Workers, pk=worker_id)
    form = NewWorkerForm(request.POST or None, instance=worker)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'manager/new_worker.html', context)


def new_worker2(request):
    form = PassportForm()
    if request.method == 'POST':
        form = PassportForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_worker_step2.html', context)


def log(request):
    orders = Orders.objects.all()
    queryset = Orders.objects.filter(
        Q(order__document_type__in=request.GET.getlist("document_type")) &
        (
            Q(order__worker__fio__contains=str(request.GET.get('search-order')).strip()) |
            Q(order_date__contains=str(request.GET.get('search-order')).strip()) |
            Q(order_number__contains=str(request.GET.get('search-order')).strip())
        )
    )
    if queryset:
        context = {'orders': queryset}
        return render(request, 'manager/log.html', context)
    else:
        context = {'orders': orders}
        return render(request, 'manager/log.html', context)


def applications(request):
    order_id_list = Orders.objects.values_list('order',flat=True)
    applications = Applications.objects.all()
    queryset = Applications.objects.filter(
        Q(document_type__in=request.GET.getlist("document_type")) &
        (
            Q(worker__fio__contains=str(request.GET.get('search-order')).strip()) |
            Q(application_date__contains=str(request.GET.get('search-order')).strip()) |
            Q(application_number__contains=str(request.GET.get('search-order')).strip())
        )
    )
    if queryset:
        context = {'applications': queryset, 'order_id_list': order_id_list}
        return render(request, 'manager/applications.html', context)
    else:
        context = {'applications': applications, 'order_id_list': order_id_list}
        return render(request, 'manager/applications.html', context)


def worker_detail(request, worker_id):
    """Рендер отдельной страницы проекта"""
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/worker_detail.html', {'workers': workers})


def orders(request):
    orders = Orders.objects.all()
    queryset = Orders.objects.filter(
        Q(order__document_type__in=request.GET.getlist("document_type")) &
        (
            Q(order__worker__fio__contains=str(request.GET.get('search-order')).strip()) |
            Q(order_date__contains=str(request.GET.get('search-order')).strip()) |
            Q(order_number__contains=str(request.GET.get('search-order')).strip())
        )
    )
    if queryset:
        context = {'orders': queryset}
        return render(request, 'manager/orders.html', context)
    else:
        context = {'orders': orders}
        return render(request, 'manager/orders.html', context)


def contracts(request):
    contracts = Contracts.objects.all()
    queryset = Contracts.objects.filter(
        Q(status__in=request.GET.getlist("status")) |
        Q(worker__fio__contains=str(request.GET.get('search-order')).strip()) |
        Q(contract_number__contains=str(request.GET.get('search-order')).strip()) |
        Q(worker__position__position_name__contains=str(request.GET.get('search-order')).strip())
    )
    if queryset:
        context = {'contracts': queryset}
        return render(request, 'manager/contracts.html', context)
    else:
        context = {'contracts': contracts}
        return render(request, 'manager/contracts.html', context)


def order_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/order_print.html', {'workers': workers})


def order_per_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/order_per_print.html', {'workers': workers})


def order_uv_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/order_uv_print.html', {'workers': workers})


def new_app(request):
    form = NewAppForm()
    if request.method == 'POST':
        form = NewAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_app.html', context)


def edit_app(request, application_id):
    app = get_object_or_404(Applications, pk=application_id)
    form = NewAppForm(request.POST or None, request.FILES or None, instance=app)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'manager/new_app.html', context)


def app_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/app_print.html', {'workers': workers})


def app_per_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/app_per_print.html', {'workers': workers})


def app_uv_print(request, worker_id):
    workers = get_object_or_404(Workers, pk=worker_id)
    return render(request, 'manager/app_uv_print.html', {'workers': workers})


def new_order(request):
    form = NewOrderForm()
    if request.method == 'POST':
        form = NewOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/new_order.html', context)


def edit_order(request, order):
    ord = get_object_or_404(Orders, pk=order)
    form = NewOrderForm(request.POST or None, request.FILES or None, instance=ord)
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


def edit_contract(request, contract_id):
    contract = get_object_or_404(Contracts, pk=contract_id)
    form = NewContractForm(request.POST or None, request.FILES or None, instance=contract)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'manager/new_contract.html', context)


def perevod(request):
    pass


def uval(request):
    pass


def not_for_hr(request):
    form = NewAppForm()
    if request.method == 'POST':
        form = NewAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/not_for_hr.html', context)
