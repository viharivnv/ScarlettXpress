
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from myR import views as myviews
from termbill import views as tbviews
from webreg import views as wbviews
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='Home'),
    path('bill/', tbviews.bill, name='Bill'),
    path('register/', wbviews.index, name='Index'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]