"""delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formpage/',views.user),
    path('thankyou/',views.thankyou),
    path('display/',views.payment),
    path('update/<int:num>/',views.update),
    path('library/',views.student),
    path('libdisplay/',views.lib_rary,name='display'),
    path('libupdate/<int:num>/',views.updatelib),
    path('libdelete/<int:num>/',views.deletelib),

]
