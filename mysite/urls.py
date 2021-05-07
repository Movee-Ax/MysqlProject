"""mysite URL Configuration

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
from django.shortcuts import HttpResponse, render, redirect
from app import views
from app import medicine
from app import firm
from app import shop
from app import worker
from app import pharmacist
# HttpResponse只能显示字符串,render可以显示html,redirect重定向


urlpatterns = [
    path('manager/', admin.site.urls),
    path('index/', views.index),            # 展示总页面，可以去选择查看什么信息
    path('register/', views.register),       # 注册
    path('login/', views.login),            # 初始登录界面
    path('logout/', views.logout),
    path('create/', views.create),
    path('show-worker/', worker.showWorker),
    path('add-worker/', worker.addWorker),
    path('edit-worker/', worker.editWorker),
    path('delete-worker/', worker.deleteWorker),
    path('show-shop/', shop.showShop),
    path('add-shop/', shop.addShop),
    path('edit-shop/', shop.editShop),
    path('delete-shop/', shop.deleteShop),
    path('show-firm/', firm.showFirm),
    path('add-firm/', firm.addFirm),
    path('edit-firm/', firm.editFirm),
    path('delete-firm/', firm.deleteFirm),
    path('show-pharmacist/', pharmacist.showPharmacist),
    path('add-pharmacist/', pharmacist.addPharmacist),
    path('edit-pharmacist/', pharmacist.editPharmacist),
    path('delete-pharmacist/', pharmacist.deletePharmacist),
    path('show-medicine/', medicine.showMedicine),
    path('add-medicine/', medicine.addMedicine),
    path('edit-medicine/', medicine.editMedicine),
    path('delete-medicine/', medicine.deleteMedicine)
]
