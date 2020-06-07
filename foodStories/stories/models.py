from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    username = models.CharField(_("Username"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    profile_img = models.ImageField(_("Profile Image"), upload_to='profile-pictures/')
    # password = models.CharField(_("Password"), max_length=50)


class Story(models.Model):
    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("Storie Imge"), upload_to = 'storie-pictures/')
    category = models.CharField(_("Category"), max_length=50)
    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Time"), auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey("stories.Author", verbose_name=_("Comment Author"), on_delete=models.CASCADE)
    post = models.ForeignKey("stories.Story", verbose_name=_("Story Comment"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    created_time = models.DateTimeField(_("Created Time"), auto_now_add=True)    
