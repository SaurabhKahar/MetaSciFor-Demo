from django.urls import path
from .views import signup_view, login_view, dashboard_view, add_income_view, add_expense_view
from django.contrib.auth.views import LogoutView
from . import views
from .views import custom_logout_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('add_income/', add_income_view, name='add_income'),
    path('add_expense/', add_expense_view, name='add_expense'),
    path('logout/', custom_logout_view, name='logout'),  

]
