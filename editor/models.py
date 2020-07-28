from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #one to many relationship
from django.urls import reverse
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta as tdelta
# from djrichtextfield.models import RichTextField

from ckeditor.fields import RichTextField
# import secretballot

class Document(models.Model):
    title = models.CharField(max_length = 100)
    # content = models.TextField()
    content = RichTextField(blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    # image = models.ImageField(blank=True,null=True,upload_to='posts_pics')
    # likes = models.PositiveIntegerField(default=0)
    # trying saving update changes
    last_change_details = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # @property
    # def image_url(self):
    #     if self.image:
    #         img = Image.open(self.image.path)
    #
    #         if img.height > 600 or img.width > 600:
    #             output_size = (400,300)
    #             img.save(self.image.path)
    #
    #
    #         return self.image.url
    #     return ''

    def save(self):
        super().save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def __str__(self): #magic methods ?
        return self.title

    def get_absolute_url(self):
        return reverse('document-detail',kwargs={'pk':self.pk})

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)
    #
    # def get_likes(self):
    #     p = self.likes
    #     number_of_likes = p.like_set.all().count()
    #     return number_of_likes
#
# class Comment(models.Model):
#     post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)#try True here
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.text
#
# # --------------- 7 July ---------------------------------
#
# class Like(models.Model):
#     '''
#     Class defines the structure of a like on a an posted Image
#     '''
#     user = models.ForeignKey(User,on_delete=models.CASCADE, null= True)
#
#     post = models.ForeignKey(Post,on_delete=models.CASCADE, null = True)
#
#     def __int__(self):
#         return self.user.username
#
#     def save_like(self):
#         self.save()
#
#     def unlike(self):
#         self.delete()
#
#     def like(self):
#         self.likes_number = 2
#         self.save()
#
#     @classmethod
#     def get_likes(cls,pk):
#         '''
#         Function that get likes belonging to a paticular posts
#         '''
#         likes = cls.objects.filter(post = pk)
#         return likes
#
#
    # class Like(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE,)
#     post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='likes')
#     # picture = models.ForeignKey(Picture)
#     created_date = models.DateTimeField(auto_now_add=True)
#     def approve(self):
#         self.approved_comment = True
#         self.save()

