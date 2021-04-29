
from django.contrib import admin
from django.urls import path

#import the loging view of user default by django
from django.contrib.auth.views import LoginView

#import urls from pagos
from django.urls import include

# url import
from django.conf.urls import url

#View from pagos app
from pagos import views

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^api/pagos/$', views.pagos_arriendos, name="pago")
]

