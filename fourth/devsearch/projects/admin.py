from django.contrib import admin
from .models import Project, Tag, Comments


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Comments)

