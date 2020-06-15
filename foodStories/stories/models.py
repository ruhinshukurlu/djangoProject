from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    username = models.CharField(_("Username"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    password = models.CharField(_("Password"), max_length=50, null=True)
    profile_img = models.ImageField(_("Profile Image"), upload_to='profile-pictures/')


class Story(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("Storie Image"), upload_to = 'storie-pictures/')

    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE)
    category = models.ManyToManyField("stories.Category", verbose_name=_(""))

    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Time"), auto_now=True)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("REcipe Image"), upload_to = 'recipe-pictures/')

    author = models.ForeignKey("stories.Author", verbose_name=_("Author"), on_delete=models.CASCADE)
    category = models.ManyToManyField("stories.Category", verbose_name=_(""))

    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Time"), auto_now=True)

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey("stories.Author", verbose_name=_("Comment Author"), on_delete=models.CASCADE)
    post = models.ForeignKey("stories.Story", verbose_name=_("Story Comment"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    created_time = models.DateTimeField(_("Created Time"), auto_now_add=True)    

    class Meta:
        ordering = ('created_time',)
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Message"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Subscribe")
        verbose_name_plural = _("Subscribes")

    def __str__(self):
        return self.name


    