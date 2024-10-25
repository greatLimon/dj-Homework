from django.shortcuts import render, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def nonePage(request):
    return HttpResponse('add parametr')

def get_recipes(request, dish):
    count_servings = request.GET.get('servings')
    if count_servings == None:
        count_servings = 1
    else: count_servings = int(count_servings)
    ingridients =  DATA[dish].copy()
    for ing_name, count in ingridients.items():
        ingridients[ing_name] = count*count_servings

    context = {
        'recipe': ingridients
    }
    return render(request, 'calculator/index.html', context)