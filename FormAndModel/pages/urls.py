from django.urls import path
from .import views
#creating urls to the actual urls..
urlpatterns=[
            path('',views.index,name='index'),
            path('user_login/',views.user_login,name='user_login')

]
