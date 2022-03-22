from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Author(models.Model):
    name = models.CharField(max_length=24, unique=True)
    identity = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="copyright")
    time_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField("Category", through="PostCategory")
    title = models.CharField(max_length=128)
    text = RichTextUploadingField()

    def get_absolute_url(self):
        return reverse('adsdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    post_ref = models.ForeignKey("Post", on_delete=models.CASCADE)
    post_category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comments(models.Model):
    to_post = models.ForeignKey("Post", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def accept_comment (self):
        self.accepted = True
        self.save()

    def __str__(self):
        return f'{self.text[0:20]}'
