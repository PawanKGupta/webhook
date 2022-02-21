"""webhook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook_authless/', include(('webhook_authless.urls', 'webhook_authless'), namespace='webhook_authless')),
    path('webhook_auth/', include(('webhook_auth.urls', 'webhook_auth'), namespace='webhook_auth')),
    path('webhook_apikey/', include(('webhook_apikey.urls', 'webhook_apikey'), namespace='webhook_apikey')),
]
