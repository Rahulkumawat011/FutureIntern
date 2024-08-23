from django.urls import path

from apps.intern import views
from apps.intern.views import Login, Sign, logout_view, HomeView

urlpatterns = [
    path('hello',views.home),
    path('login_view/', Login.as_view(),name='login_view'),
    path('sign/', Sign.as_view(),name='signup'),
    path('logout/user/', logout_view, name='logout_user'),
    path('dashboard/', HomeView.as_view(), name='home'),

]