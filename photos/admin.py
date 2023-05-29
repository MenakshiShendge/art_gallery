from django.contrib import admin

# Register your models here.
from .models import Photo,Category,Comment,profile,urequesr,artistname

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(profile)
admin.site.register(urequesr)
admin.site.register(artistname)
