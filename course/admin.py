from django.contrib import admin
from course.models import Course,Tag,Learning,Prerequisite,Video,Contact,MyProfile
# Register your models here.


class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

    class Media:
        js = ('js/tinyInject.js',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin ,PrerequisiteAdmin ,VideoAdmin]
    prepopulated_fields = {'slug':('name',)}


class Video1Admin(admin.ModelAdmin):
    model = Video

    class Media:
        js = ('js/tinyInject.js',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    list_filter = ('Timestamp', )
    search_fields = ['email','name','phone']


admin.site.register(Video,Video1Admin)
admin.site.register(Tag)
admin.site.register(Contact,ContactAdmin)
admin.site.register(MyProfile)