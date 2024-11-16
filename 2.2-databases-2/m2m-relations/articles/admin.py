from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, TagsArticles

class TagsArticlesInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True and is_main == False:
                is_main = True
            elif form.cleaned_data.get('is_main') == True and is_main == True:
                raise ValidationError('Основной тэг должен быть всегда один!')
        if not is_main:
            raise ValidationError('Укажите хотябы один основной тэг!')
        return super().clean()

class TagsArticlesInline(admin.TabularInline):
    model = TagsArticles
    formset = TagsArticlesInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsArticlesInline]

@admin.register(Tags)
class TagsAdm(admin.ModelAdmin):
    pass
