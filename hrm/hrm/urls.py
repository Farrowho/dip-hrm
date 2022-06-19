from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new_worker/', views.new_worker, name='new_worker'),
    path('new_worker/<int:worker_id>/', views.edit_worker, name='edit_worker'),
    path('new_worker_step2/', views.new_worker2, name='new_worker2'),
    path('log/', views.log, name='log'),
    path('applications/', views.applications, name='applications'),
    path('app_print/<int:worker_id>/', views.app_print, name='app_print'),
    path('app_per_print/<int:worker_id>/', views.app_per_print, name='app_per_print'),
    path('app_uv_print/<int:worker_id>/', views.app_uv_print, name='app_uv_print'),
    path('worker_detail/<int:worker_id>/', views.worker_detail, name='worker_detail'),
    path('orders/', views.orders, name='orders'),
    path('order_print/<int:worker_id>/', views.order_print, name='order_print'),
    path('order_per_print/<int:worker_id>/', views.order_per_print, name='order_per_print'),
    path('order_uv_print/<int:worker_id>/', views.order_uv_print, name='order_uv_print'),
    path('new_order/', views.new_order, name='new_order'),
    path('new_order/<int:order>/', views.edit_order, name='edit_order'),
    path('new_app/', views.new_app, name='new_app'),
    path('new_app/<int:application_id>/', views.edit_app, name='edit_app'),
    path('contracts/', views.contracts, name='contracts'),
    path('contracts/filter/', views.contracts, name='filter_contracts'),
    path('new_contract/', views.new_contract, name='new_contract'),
    path('new_contract/<int:contract_id>/', views.edit_contract, name='edit_contract'),
    path('applications/filter/', views.applications, name='filter'),
    path('orders/filter/', views.orders, name='filter_orders'),
    path('log/filter/', views.log, name='filter_log'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
