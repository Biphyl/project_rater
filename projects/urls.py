"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from rates.views import ProfileViewset,PostViewset

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewset)
router.register(r'posts', PostViewset)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',include('rates.urls')),
    path(r'',include(router.urls)),
    path(r'accounts/', include('django_registration.backends.one_step.urls')),
    path(r'logout/', views.LogoutView, {"next_page": '/'}),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    path(r'api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
