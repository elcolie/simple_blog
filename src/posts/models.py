from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    logo_image = models.ImageField(upload_to='documents/%Y/%m/%d',
                                   blank=True,
                                   null=True,
                                   help_text="200x200 pixels image")  # pip install Pillow

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
