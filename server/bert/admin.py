from django.contrib import admin

from .models import Bert

admin.site.register(Bert)

# Allows the Model to be administered via the /admin interface
# Highly recommendeded for easier debug
