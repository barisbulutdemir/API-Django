from django.contrib import admin
from .models import Note, Category

class NoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('body',)

admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
