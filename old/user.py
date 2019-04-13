""" Posts models """

# Django
from django.db import models

# DJANGO por default agrega un id
class User(models.Model):
  
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  biography = models.TextField(blank=True)
  birthdate = models.DateField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True) # En cuando se persista en DB, le asignara la fecha actual
  modified = models.DateTimeField(auto_now=True) # Fecha en la que se edito por ultima vez
  is_admin = models.BooleanField(default=False)
  country = models.CharField(max_length=50, null=True)
  state = models.CharField(max_length=50, null=True)
  city = models.CharField(max_length=50, null=True)

  def __str__(self):
    ''' Return email '''
    return self.email
