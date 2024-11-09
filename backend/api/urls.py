"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.urls import path
from .views import (
    test_api_view,
    get_customer_orders,
    add_order,
    delete_order,
    update_order,
    get_all_orders,
)

urlpatterns = [
    # API entry points should be defined here
    path("test.json", test_api_view, name="api_test"),
    path("customer_orders/<int:customer_id>", get_customer_orders, name="get_customer_orders"),
    path('addOrder',add_order,name='add_order'),
    path("deleteOrder/<int:order_id>", delete_order, name="delete_order"),
    path("updateOrder/<int:order_id>", update_order, name="update_order"),
    path("allOrders", get_all_orders, name="all_orders"),
]

