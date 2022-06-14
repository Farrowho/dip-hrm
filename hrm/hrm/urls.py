from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new_worker/', views.new_worker, name='new_worker'),
    path('new_worker_step2/', views.new_worker2, name='new_worker2'),
    path('log/', views.log, name='log'),
    path('applications/', views.applications, name='applications'),
    path('worker_detail/<int:worker_id>/', views.worker_detail, name='worker_detail'),
    path('orders/', views.orders, name='orders'),
    path('order_print/<int:worker_id>/', views.order_print, name='order_print'),
    path('new_order/', views.new_order, name='new_order'),
    path('new_app/', views.new_app, name='new_app'),
    path('contracts/', views.contracts, name='contracts'),
    path('new_contract/', views.new_contract, name='new_contract')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
