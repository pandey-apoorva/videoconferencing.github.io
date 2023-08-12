from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('joinroom/',views.join_room, name='joinroom'),
    path('logout/',views.logout_view, name='logout'),
    # path('',views.index, name='index'),

]