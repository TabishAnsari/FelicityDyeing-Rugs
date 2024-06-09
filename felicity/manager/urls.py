from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("createInvoice", views.createInvoice, name="createInvoice"),
    path("createChallan", views.createChallan, name="createChallan"),
    path("createBuyer",views.createBuyer, name="createBuyer"),
    path("invoice", views.invoice, name="invoice"),
    path("challan", views.challan, name="challan"),
]