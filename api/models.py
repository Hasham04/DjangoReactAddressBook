from django.db import models
from django.contrib.auth.models import User

class AddressBook(models.Model):
  user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
  name = models.CharField(max_length=200,blank=False,null=True)
  address = models.CharField(max_length=300,blank=False,null=True)
  phone = models.CharField(max_length=15,blank=False,null=True)
  email = models.EmailField(max_length=254,blank=False)
  favorite=models.BooleanField(blank=False)

  def __str__(self):
    return self.name