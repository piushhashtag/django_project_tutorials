from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .choices import CHOICES
from django.conf import settings


# Create your models here.
class File(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	file = models.FileField(null=True, blank=True)

	def __str__(self):
		return str(self.id)


class Comment(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	# parent = models.ForeignKey("self", null=True, blank=True)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	# objects = CommentManager()

	class Meta:
		ordering = ['-timestamp']

	def __unicode__(self):
		return str(self.object_id)


class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField()
	Subject = models.IntegerField(choices=CHOICES)
	message=models.TextField()


	def __str__(self):
		return self.name
