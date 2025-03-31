from django.contrib import admin
from .models import Member, Sermon, Give, Event, WelcomeContent

# Register Event Model
admin.site.register(Event)

# Customizing Sermon Admin View
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')

# Register Other Models
admin.site.register(Member)
admin.site.register(Give)
admin.site.register(Sermon, SermonAdmin)

# Register WelcomeContent Model for Managing Welcome Images & Verses
@admin.register(WelcomeContent)
class WelcomeContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'verse')
    search_fields = ['verse']  # Allows searching by verse text
