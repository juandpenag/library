from django.contrib import admin
from .models import Books, Authors, Publishers

# Register your models here.
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Publishers)