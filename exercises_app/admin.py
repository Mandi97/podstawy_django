from django.contrib import admin

# Register your models here.
from exercises_app.models import Band, Album, Category, Article

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Article)
admin.site.register(Category)
