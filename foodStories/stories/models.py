from django.db import models
from django.utils.translation import ugettext as _

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class AddResult(models.Model):
    result = models.IntegerField(_("Result"))

    def __str__(self):
        return str(self.result)

class countStory(models.Model):
    story_count = models.IntegerField(_("Story Count"))

    def __str__(self):
        return str(self.story_count)
        

class Story(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("Storie Image"), upload_to = 'storie-pictures/', blank=True, null=True)
    
    author = models.ForeignKey("account.MyUser", verbose_name=_("Author"), on_delete=models.CASCADE, null=True, related_name = 'stories')
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name = 'stories')

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
    recipe_img = models.ImageField(_("Recipe Image"), upload_to = 'recipe-pictures/', blank=True, null=True)

    author = models.ForeignKey("account.MyUser", verbose_name=_("Author"), on_delete=models.CASCADE, null = True, related_name = 'recipes')
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank = True, null = True, related_name = 'recipes')

    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Time"), auto_now=True)

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey("account.MyUser", verbose_name=_("Comment Author"), on_delete=models.CASCADE)
    post = models.ForeignKey("stories.Story", verbose_name=_("Story Comment"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    created_time = models.DateTimeField(_("Created Time"), auto_now_add=True)    

    class Meta:
        ordering = ('created_time',)
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    category_img = models.ImageField(_("Category Image"), upload_to='category-pictures/')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50,blank = True)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50,blank = True)
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


class StaticInfo(models.Model):
    address = models.CharField(_("Address"), max_length=100)
    contact_number = models.CharField(_("Contact Number"), max_length=50)
    email_address = models.EmailField(_("Email Address"), max_length=254)
    website = models.CharField(_("Website"), max_length=50)
    
    class Meta:
        verbose_name = _("StaticInfo")
        verbose_name_plural = _("StaticInfos")

    def __str__(self):
        return self.email_address


class Tag(models.Model):

    title = models.CharField(_("Tag title"), max_length=50)
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    price = models.IntegerField(_("Price"), default = 0)
    image = models.URLField(_("Image"), max_length=200)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.title
    
