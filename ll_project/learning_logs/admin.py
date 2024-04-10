from django.contrib import admin
from .models import Topic
from .models import Entry

# Register your models here.
class topicAdmin(admin.ModelAdmin):
  list_display=("text","date_added")
admin.site.register(Topic,topicAdmin)
admin.site.register(Entry)
