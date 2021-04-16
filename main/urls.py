


"""
<< --------------------------------------------------------------------------------------------------------------------

        @ Author = Convertopedia
        Copyright © 2021 Convertopedia to Present
        All rights reserved

<< --------------------------------------------------------------------------------------------------------------------
"""


# from django.contrib import admin
from django.urls import path
from . import views


# ----------------------------------------------------------------------------------------------------------------------
        # ************************************************************

"""                 Creating URL Patterns                                                                            """

        # *************************************************************
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.auth, name='auth'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('forgotpassword/', views.forgetpassword, name='forgetpassword')
]

