from django.urls import path
from busses import views
urlpatterns=[
    path('route',views.fun),
]