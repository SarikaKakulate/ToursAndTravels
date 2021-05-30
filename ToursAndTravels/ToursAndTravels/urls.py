"""ToursAndTravels URL Configuration

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
from django.urls import path,include

#load static image below 4 packages
from django.conf.urls.static import static
from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tourapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    
    path('index/', views.index,name='index'),   #home page

    path('addcar/',views.addcar,name='addcar'), #add car

    path('showcar/',views.showcar,name='showcar'),    #display cars that we added

    path('update/<int:car_id>',views.update_car,name='update'),


    path('delete/<int:car_id>',views.delete,name='delete'),

    path('accounts/', include('django.contrib.auth.urls')),

      path('logout/', views.logout),



]

#for static image 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


