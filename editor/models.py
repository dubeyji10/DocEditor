from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #one to many relationship
from django.urls import reverse
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta as tdelta
# from djrichtextfield.models import RichTextField
from django.core.files import File
from django.utils import timezone
from urllib.request import urlretrieve
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
    # last_change_details = []
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

    # signed_file = models.FileField(upload_to="docs/%Y-%m-%d%/%H-%M-%S/",blank=True, null=True)
    #
    #
    # def download_to_local(self,url):
    #     name, _ = urlretrieve(url)
    #     self.signed_file.save("{}.pdf".format(timestamp=timezone.now().strftime('%Y-%m-%d%/%H-%M-%S')),File(open(name, 'rb')))
    #     print("------  saved   ------")