""" User views """

# Django
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse_lazy
# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
# Exceptions
from django.db.utils import IntegrityError
# Utils
from pdb import set_trace
# Forms
from users.forms import ProfileForm, SignUpForm

class LoginView(auth_views.LoginView):
  """ Login view """
  template_name = 'users/login.html'


def login_view(request):
  """ Login view """
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
      login(request,user)
      return redirect('posts:feed')
    else:
      return render(request, 'users/login.html', { 'error': 'Invalid username and password'})
  else:
    return render(request, 'users/login.html') # users/login.html


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
  """ Logout view """
  template_name = 'users/logout.html'


@login_required
def logout_view(request):
  """ Logout request """
  logout(request)
  return redirect('users:login')


class UserDetailView(DetailView):
  """ User detail view """
  template_name = 'users/detail.html'
  slug_url_kwarg = 'username'
  slug_field = 'username'
  queryset = User.objects.all()
  context_object_name='name'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.get_object()
    context['posts'] = Post.objects.filter(user=user).order_by('created')
    return context


class SignUpView(FormView):
  """ User signup view """

  template_name = 'users/signup.html'
  form_class = SignUpForm
  success_url = reverse_lazy('users:login')

  # Have to overwrite this to make an action once the form is validated
  def form_valid(self, form):
    """ Save form data """
    form.save()
    return super().form_valid(form)


# def signup_view(request):
#   """ Sign up view """
#   if request.method == 'POST':
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('login')
  
#   else:
#     form = SignUpForm()

#   return render(
#     request, 
#     'users/signup.html',
#     context={'form':form}
#   )

class UpdateProfileView(LoginRequiredMixin, UpdateView):
  """ Update profile view """

  template_name = 'users/update_profile.html'
  model = Profile
  fields = ['website', 'biography', 'phone_number', 'picture']

  def get_object(self):
    """ Return user's profile """
    return self.request.user.profile

  def get_success_url(self):
    """ Return to user's profile """
    username = self.object.user.username
    return reverse('users:detail', kwargs={'username': username})

# @login_required
# def update_profile(request):
#   """ Update a user's profile view """
#   user = request.user
#   profile = user.profile
#   if request.method == 'POST':
#     form = ProfileForm(request.POST, request.FILES) # In request.FILES is the multipart
#     if form.is_valid():
#       data = form.cleaned_data
#       profile.website = data['website']
#       profile.phone_number = data['phone_number']
#       profile.biography = data['biography']
#       profile.picture = data['picture']
#       profile.save()

#       url = reverse('users:detail', kwargs={'username': request.user.username})
#       return redirect(url)
#   else:
#     form = ProfileForm()

#   return render(
#     request, 
#     'users/update_profile.html',
#     {
#       'user': user,
#       'profile': profile,
#       'form':form
#     })
