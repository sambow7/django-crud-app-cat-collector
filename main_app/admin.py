# Add to the import
from django.contrib import admin
from .models import Cat, Feeding, Toy

# Register the new model
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
