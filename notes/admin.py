from django.contrib import admin
from .models import *

class NotesAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'subject', 'filetype', 'status', 'uploadingdate')
# Register your models here.
admin.site.register(Signup)
admin.site.register(Notes, NotesAdmin)