from django.contrib import admin

# Register your models here.
from core.models import Creative, CreativeLabeling


admin.site.register(Creative)
admin.site.register(CreativeLabeling)
