from django.contrib import admin

from .models import Article, Tags, TagsArticles


class TagsArticlesInline(admin.TabularInline):
    model = TagsArticles
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsArticlesInline, ]

@admin.register(Tags)
class TagsAdm(admin.ModelAdmin):
    pass
