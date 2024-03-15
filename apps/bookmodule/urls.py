from django.urls import path
from apps.bookmodule import views
urlpatterns = [
 path('',views.index,name='index')
]
