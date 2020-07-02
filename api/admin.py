from django.contrib import admin
from .models import Movie, Rating, Comment

admin.site.register(Movie)
admin.site.register(Rating)


@admin.register(Comment)  # admin decorators
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'message')
