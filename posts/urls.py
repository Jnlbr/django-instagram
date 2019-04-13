
# Django
from django.urls import path

# Views
from posts import views

# Views
urlpatterns = [

  path(
    route='',
    view=views.PostFeedView.as_view(),
    name='feed'
  ),
  path(
    route='posts/new/',
    view=views.CreatePostView.as_view(),
    name='create'
  ),
  path(
    route='<int:pk>',
    view=views.PostDetailView.as_view(),
    name='detail'
  )

]