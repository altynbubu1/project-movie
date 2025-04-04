from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'country', 'budget', 'category', 'draft')
    list_filter = ('year', 'country', 'category')
    search_fields = ('title', 'description', 'year')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)