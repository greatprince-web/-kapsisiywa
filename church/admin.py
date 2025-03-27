from django.contrib import admin
from .models import Member, Sermon, Give
# admin.py in the church app
from django.contrib import admin
from .models import Event

admin.site.register(Event)

# admin.py
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')
admin.site.register(Member)
admin.site.register(Give)
admin.site.register(Sermon, SermonAdmin)
