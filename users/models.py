''' Users models '''

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
  ''' Profile model 
  Proxy model that extends the base data with other information
  '''
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.URLField(max_length=256, blank=True)
  biography = models.TextField(blank=True,null=True)
  phone_number = models.CharField(max_length=16, blank=True)
  # BASE_DIR == MEDIA_URL (Only for media files)
  picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    ''' Return username '''
    return self.user.email
