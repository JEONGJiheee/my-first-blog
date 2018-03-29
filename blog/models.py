from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE) 
	title = models.CharField(max_length=200) #글자수가 제한된 텍스트 정의
	text = models.TextField()  # 글자 수에 제한이 없는 긴 텍스트
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title