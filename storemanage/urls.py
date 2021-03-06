"""storemanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from store_manage.views import StoreListView, StoreDetailView, PopoverHtmlView, TopStar,OpenAndCloseStores

urlpatterns = [
    path('', StoreListView.as_view()),
    path('admin/', admin.site.urls),
    path('store/', StoreListView.as_view(), name='store'),
    path('store/<slug>', StoreDetailView.as_view(), name='detail'),
    path('open_close_stores', OpenAndCloseStores.as_view(), name='oc'),
    path('popoverHtml/<slug>', PopoverHtmlView.as_view(), name='Popover'),
    path('top_star/<slug>', TopStar.as_view(), name='top_star'),
]
