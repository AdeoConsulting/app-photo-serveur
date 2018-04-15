from django.db import models

class Photo (models.Model):
	photo = models.ImageField(upload_to="photos/")
	created_at = models.DateTimeField(auto_now_add=True)