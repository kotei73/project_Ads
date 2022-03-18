from django.contrib import admin

from .models import Ads, Rubric

# Register your models here.

class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric',)
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Ads, AdsAdmin)
admin.site.register(Rubric)
