from django.db import models
from datetime import datetime
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     priority = models.IntegerField(default=0)
#     website = models.URLField(blank=True)
#     def __str__(self):
#         return self.user.name

class chat(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    time =  models.DateTimeField('date published',null=True)
    # time.editable = True
    def __str__(self):
        return str(id)
