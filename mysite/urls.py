
"""
<< --------------------------------------------------------------------------------------------------------------------

        @ Author = Convertopedia
        Copyright © 2021 Convertopedia to Present
        All rights reserved

<< --------------------------------------------------------------------------------------------------------------------
"""

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# ----------------------------------------------------------------------------------------------------------------------
""" 
This  URL program for our Django project
        * Here we can directly create the URL pattern for our app
        * But the Django project may contain more then one app in a single django project
        * So, to avoid overlapping of URL we are creating separate url py file in each app and finally we can include it
          to the Django project 
"""
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls') )
]
