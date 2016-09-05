from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class Task(models.Model):
#     summary = models.CharField(max_length=32)
#     content = models.TextField()
#     reported_by = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         permissions = (
#             ('view_task', 'View task'),
#         )
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=32)
#     owned_by = models.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         permissions = (
#             ('view_product', 'View product'),
#         )
#
#
# class Post(models.Model):
#     title = models.CharField('title', max_length=64)
#     slug = models.SlugField(max_length=64)
#     content = models.TextField('content')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         permissions = (
#             ('view_post', 'View post'),
#         )
#         get_latest_by = 'created_at'
#
#     def __str__(self):
#         return self.title
#
#     @models.permalink
#     def get_absolute_url(self):
#         return {'post_slug': self.slug}
