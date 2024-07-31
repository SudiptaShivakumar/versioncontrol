from django.contrib import admin
from .models import Repository, File, Version

admin.site.register(Repository)
admin.site.register(File)
admin.site.register(Version)
