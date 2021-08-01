from django.contrib import admin

# Register your models here.
from blog.models import post,Catagory

class Adminpost(admin.ModelAdmin):
    list_display = ['post_id','title']
    list_filter = ('status', 'timeStamp', 'author','catagory')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = ('blog/js/tinymce.js',)




admin.site.register(post ,Adminpost)
admin.site.register(Catagory)


