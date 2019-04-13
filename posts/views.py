""" Posts views """

# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
# Models
from posts.models import Post
# Forms
from posts.forms import PostForm
# Utilities
from datetime import datetime

class PostDetailView(LoginRequiredMixin, DetailView):
  """ Return post detail """
  template_name = 'posts/detail.html'
  queryset = Post.objects.all()
  context_object_name = 'post'


class PostFeedView(LoginRequiredMixin, ListView):
  """ Return all published posts """
  template_name = 'posts/feed.html'
  model = Post
  ordering = ['-created']
  paginate_by = 15
  context_object_name = 'posts'


@login_required
def list_posts(req):
  posts = Post.objects.all().order_by('created')
  return render(req, 'posts/feed.html', {'posts':posts})



class CreatePostView(LoginRequiredMixin, CreateView):
  """ Create a new post """
  template_name = 'posts/new.html'
  form_class = PostForm
  success_url = reverse_lazy('posts:feed')

  def get_context_data(self, **kwargs):
    """" Add user and profile to context """
    context = super().get_context_data(**kwargs)
    context['user'] = self.request.user
    context['profile'] = self.request.user.profile
    return context


@login_required
def create_post(req):
  """ Create new posts view """
  if(req.method == 'POST'):
    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
      form.save()
      return redirect('posts:feed')
  
  else:
    form = PostForm()

  return render(
    request=req,
    template_name='posts/new.html',
    context={
      'form':form,
      'user':req.user,
      'profile':req.user.profile
    }
  )