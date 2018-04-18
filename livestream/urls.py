from livestream import views
from django.urls import path
# from django.conf.urls import include

urlpatterns = [
    path('',views.index,name='index'),
    path('update/',views.update,name='update'),
]
