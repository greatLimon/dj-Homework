from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    tag_id = request.GET.get('tag_id')
    if tag_id:
        query = Article.objects.filter(scopes__tag__id = tag_id)
    else:
        query = Article.objects.all()
    data = query.all()
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    data.order_by(ordering)
    context = {
        'object_list' : data
    }

    return render(request, template, context)
