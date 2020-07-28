
# Register your models here.
# from django.contrib import admin
# from .models import Document

# Register your models here.

# admin.site.register(Document)

from django.contrib import admin
from .models import Document

# admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date_posted')
    list_filter = ("date_posted",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'title': ('title',)}

admin.site.register(Document, DocumentAdmin)