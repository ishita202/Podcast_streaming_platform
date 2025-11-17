from django.urls import path
from .views import user_login, user_signup, logout_view, welcome_view,home_view
from authentication.views import welcome_view

app_name = "authentication"
urlpatterns = [
    path('welcome/', welcome_view, name='welcome'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),

]
