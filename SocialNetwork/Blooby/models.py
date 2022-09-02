# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(default='Hola, este es mi Blooby!!!', max_length=100)
	image = models.ImageField(default='default.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
									.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
									.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)
	



class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField(max_length=300)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	liked = models.ManyToManyField(User, default=None, blank=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content

	@property
	def num_likes(self):
		return self.liked.all().count()

LIKE_CHOICES = (
	('Like', 'Like'),
	('Unlike', 'Unlike'),
)

class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES ,default='Like', max_length=10)

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.ForeignKey(User,related_name="user_name" , on_delete=models.CASCADE)
	body = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)








