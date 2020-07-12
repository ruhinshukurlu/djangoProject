from django.contrib import admin
from stories.models import Story,Recipe,Category,Comment,Contact,Subscribe, Car
# Register your models here.



@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    ordering = ('title',)
    search_fields = ('title','author','category')
    list_filter = ('created_at',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    ordering = ('title',)
    search_fields = ('title','author','category')
    list_filter = ('created_at',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','post','text',)
    ordering = ('created_time',)
    search_fields = ('author','post','text',)
    list_filter = ('created_time',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message',)
    ordering = ('subject',)
    search_fields = ('name','email','subject',)

    fieldsets = (
        ('Required Information', {
            'description' : 'These fields are required',
            "fields": ('email','message',),
        }),
        ('Optional Information', {
            'classes' : ('collapse',),
            "fields": ('name','subject',),
        }),
    )


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    ordering = ('email',)
    search_fields = ('email',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','image',)
    
