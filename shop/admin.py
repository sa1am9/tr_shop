from django.contrib import admin
from .models import Board, Rubric

class BoardAdmin(admin.ModelAdmin):
    list_display =  ('title', 'published', 'price', 'content', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Board, BoardAdmin)
admin.site.register(Rubric)