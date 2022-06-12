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
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
