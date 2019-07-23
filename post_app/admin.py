from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PostTag, Post, PostComment, PostReComment, ChemicalTag
from django_summernote.admin import SummernoteModelAdmin

class PostModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'




admin.site.register(Post, PostModelAdmin)
admin.site.register(PostTag)
admin.site.register(ChemicalTag)
admin.site.register(PostComment)
admin.site.register(PostReComment)
