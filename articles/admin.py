from django.contrib import admin
from .models import Article, Coment

# Register your models here.

class ComentInLine(admin.StackedInline):
    model = Coment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ComentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Coment)