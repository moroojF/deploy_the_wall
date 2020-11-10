from django.db import models
from login_reg_app.models import Users

# Create your models here.
class Messages(models.Model):
    user_id = models.ForeignKey(Users, related_name="message1", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    message_id = models.ForeignKey(Messages, related_name="comment1", on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users, related_name="comment2", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)