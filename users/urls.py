# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns = [
  # Posts
  #Managment
  path(
    'login/', 
    view=views.LoginView.as_view(),
    name='login'
  ),
  path(
    'logout/', 
    view=views.LogoutView.as_view(),
    name='logout'
  ),
  path(
    'signup/', 
    view=views.SignUpView.as_view(), 
    name='signup'
  ),
  path(
    'me/profile/',
    view=views.UpdateProfileView.as_view(), 
    name='update'
  ),
  path(
    route='<str:username>/',
    # Class-based view
    # view=TemplateView.as_view(template_name='users/detail.html'),
    view=views.UserDetailView.as_view(),
    name='detail'
  ),
]