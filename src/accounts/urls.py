from django.urls import path,re_path,include

urlpatterns = [
    path('accounts/',include('allauth.urls')),
]
