from django.contrib import admin
from .models import Review, StreamPlatform, WatchList

# Register your models here.
class WatchListAdmin(admin.ModelAdmin):

    list_display = ('title', 'storyline', 'active',)
    list_filter = ('active',)
    ordering = ('title',)
    search_fields = ('title',)
    list_per_page = 20


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('watchlist', 'rating', 'created', 'updated', 'active', )
    list_filter = ('created',)
    ordering = ('-updated',)
    search_fields = ('watchlist',)
    list_per_page = 20


class StreamPlatformAdmin(admin.ModelAdmin):

    list_display = ('name', 'about', 'website',)
    ordering = ('name',)
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(WatchList, WatchListAdmin)
admin.site.register(StreamPlatform, StreamPlatformAdmin)
admin.site.register(Review, ReviewAdmin)
