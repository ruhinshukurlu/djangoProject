from django.db import models
from django.utils.translation import ugettext as _

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.


# class Author(models.Model):
#     first_name = models.CharField(_("First Name"), max_length=50,blank = True)
#     last_name = models.CharField(_("Last Name"), max_length=50,blank = True)
#     username = models.CharField(_("Username"), max_length=50)
#     email = models.EmailField(_("Email"), max_length=254)
#     password = models.CharField(_("Password"), max_length=50, null=True)
#     profile_img = models.ImageField(_("Profile Image"), upload_to='profile-pictures/',blank = True)

#     class Meta:
#         verbose_name = _("Author")
#         verbose_name_plural = _("Authors")

#     def __str__(self):
#         return self.username


class Story(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("Storie Image"), upload_to = 'storie-pictures/', blank=True, null=True)

    author = models.ForeignKey("account.MyUser", verbose_name=_("Author"), on_delete=models.CASCADE, null=True, related_name = 'stories')
    highlighted = models.TextField()
    category = models.ForeignKey("stories.Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank=True, null=True, related_name = 'stories')

    created_at = models.DateTimeField(_("Created Time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Time"), auto_now=True)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
            Use the `pygments` library to create a highlighted HTML
            representation of the story.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Story, self).save(*args, **kwargs)

class Recipe(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    storie_img = models.ImageField(_("Recipe Image"), upload_to = 'recipe-pictures/')

    author = models.ForeignKey("account.MyUser", verbose_name=_("Author"), on_delete=models.CASCADE)
    category = models.ManyToManyField("stories.Category", verbose_name=_(""))

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

    