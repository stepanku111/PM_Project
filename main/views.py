from django.shortcuts import render
from main.models import Boot, Accessory, Hat, LowerOuter, UnderPants, Pants, OuterWear


def index(request):
    return render(request, 'html/index.html')


accessory_name = ('ремень', 'сумка', 'рюкзак', 'шарф', 'перчатки', 'варежки', 'носочки', 'резинк для волос', 'ободок', 'тапочки', 'тапки', 'платок', 'пояс', 'браслет', 'заколк', 'панно', 'наволочк', 'трусики', 'штанишки', 'комплект для девочки', 'плавки для', 'волос', 'салфет', 'матрас', 'покрывало', 'штаны', 'песочник')
boot_names = ('дутики', 'туфли', 'балетки', 'полуботинки', 'босоножки', 'резиновые сапоги', 'сандали', 'ботинки', 'ботфорты', 'кеды', 'кроссовки', 'полусапоги', 'ботильоны', 'сабо', 'мокасины', 'сапоги', 'угги', 'тапки', 'валенки', 'сланцы')
hat_names = ('кепка', 'шапка', 'шляпа', 'панама')
lower_outer_names = ('шорты', 'джемпер', 'поло', 'футболка', 'блузка', 'рубашка', 'рубашечка', 'платье', 'майка', 'пижама', 'топ', 'боди', 'жакет', 'толстовка', 'свитер', 'пиджак', 'кардиган', 'водолазка', 'брюки', 'бомбер', 'ночная сорочка', 'кофта', 'юбка', 'туника', 'костюм', 'халат', 'комплект трикотажный', 'сарафан', 'распашонка', 'свитшот', 'сорочка', 'салфетка гобеленовая', 'пуловер', 'покрывало', 'простыня', 'подушка', 'пеленка', 'блуза', 'комплект женский', 'бюстгальтер', 'набор пеленок')
under_pants_names = ('носки', 'носков', 'подследники', 'трусы', 'трусов', 'колготки', 'набор тонких ремней', 'набор из 6 заколок для волос', 'набор заколок для волос', 'набор резинок для волос', 'набор резинок-пружинок для волос', 'набор из 10 резинок для волос', 'набор бижутерии для девочек', 'набор обручей для волос', 'набор крестильный', 'набор 3 предмета (ситец) 20', 'следки женские', 'набор на выписку', 'набор пеленок', 'панталоны женские', 'набор 3 предмета (фланель)', 'набор 2 предмета (фланель)', 'столовый набор', 'набор салфеток', 'набор для сауны', 'набор столового белья', 'следки', 'набор чехлов на стул', 'кофточки', 'штанишки', 'набор для спальни', 'набор из шитья', 'набор пелёнок', 'набор 9 предметов с пододеяльником "детство"')
pants_names = ('брюки', 'юбка', 'шорты', 'джинсы', 'лосины', 'легинсы', 'леггинсы', 'кальсоны', 'сарафан', 'трегинсы', 'джоггеры', 'кюлоты', 'бриджи', 'капри')
outer_wear_names = ('куртка', 'ветровка', 'полукомбинезон', 'комбинезон', 'жилет', 'пальто', 'пуховик', 'парка', 'плащ', 'бриджи', 'платье', 'костюм детский', 'колготки')

SYMBOLS_SIZES = ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')


def result(request):
    if request.GET['user-request'].lower() in boot_names:
        model_name = Boot
    elif request.GET['user-request'].lower() in accessory_name:
        model_name = Accessory
    elif request.GET['user-request'].lower() in outer_wear_names:
        model_name = OuterWear
    elif request.GET['user-request'].lower() in hat_names:
        model_name = Hat
    elif request.GET['user-request'].lower() in lower_outer_names:
        model_name = LowerOuter
    elif request.GET['user-request'].lower() in under_pants_names:
        model_name = UnderPants
    elif request.GET['user-request'].lower() in pants_names:
        model_name = Pants
    else:
        model_name = Boot

    if request.GET['sorting-type'] is not None:
        if request.GET['sorting-type'] == 'Price ASC':
            order_by = 'price'
        elif request.GET['sorting-type'] == 'Price DESC':
            order_by = '-price'
        elif request.GET['sorting-type'] == 'Discount DESC':
            order_by = '-discount'
    else:
        order_by = 'price'

    sizes = request.GET['user-size'].split(',')
    user_size = []
    for size in sizes:
        user_size.append(size)

    search_result = []
    if type(user_size) is list:
        for size in user_size:
            for item in model_name.objects.filter(
                name__contains=request.GET['user-request'], size__contains=size, price__range=(
                    int(request.GET['min-price']), int(request.GET['max-price'])
                )
            ).order_by(order_by):
                search_result.append(item)
    else:
        search_result = model_name.objects.filter(
            name__contains=request.GET['user-request'], size__contains='', price__range=(
                request.GET['min-price'], request.GET['max-price']
            )
        ).order_by(order_by)

    size_list = []
    for item in search_result:
        sizes = item.size.split(',')
        for size in sizes:
            size = size.strip()
            if size not in size_list:
                size_list.append(size)

    contex = {
        'user_request': request.GET['user-request'],
        'user_size': request.GET['user-size'],
        'db_response_items': search_result[(int(request.GET['page']) - 1) * 12:int(request.GET['page']) * 12],
        'page': int(request.GET['page']),
        'last_page': len(search_result) / 12,
        'previous_page': int(request.GET['page']) - 1 if int(request.GET['page']) > 2 else 1,
        'next_page': int(request.GET['page']) + 1,
        'size_list': sorted(size_list),
        'min_price': request.GET['min-price'],
        'max_price': request.GET['max-price'],
        'sorting_type': request.GET['sorting-type'],
        'discount_only': request.GET['discount-only'],
    }
    return render(request, 'html/result.html', contex)


def filter(request):
    if request.GET['user-request'].lower() in boot_names:
        model_name = Boot
    elif request.GET['user-request'].lower() in accessory_name:
        model_name = Accessory
    elif request.GET['user-request'].lower() in outer_wear_names:
        model_name = OuterWear
    elif request.GET['user-request'].lower() in hat_names:
        model_name = Hat
    elif request.GET['user-request'].lower() in lower_outer_names:
        model_name = LowerOuter
    elif request.GET['user-request'].lower() in under_pants_names:
        model_name = UnderPants
    elif request.GET['user-request'].lower() in pants_names:
        model_name = Pants
    else:
        model_name = LowerOuter

    if request.GET['sorting-type'] is not None:
        if request.GET['sorting-type'] == 'Price ASC':
            order_by = 'price'
        elif request.GET['sorting-type'] == 'Price DESC':
            order_by = '-price'
        elif request.GET['sorting-type'] == 'Discount DESC':
            order_by = '-discount'
    else:
        order_by = 'price'

    user_size = 0
    if len(request.GET['user-size']) > 0:
        sizes = request.GET['user-size'].split(',')
        user_size = []
        for size in sizes:
            user_size.append(int(size.strip()))

    search_result = []
    if type(user_size) is list:
        for size in user_size:
            for item in model_name.objects.filter(
                name__contains=request.GET['user-request'], size__contains=size, price__range=(
                    int(request.GET['min-price']), int(request.GET['max-price'])
                )
            ).order_by(order_by):
                search_result.append(item)
    else:
        search_result = model_name.objects.filter(
            name__contains=request.GET['user-request'], size__contains='', price__range=(
                request.GET['min-price'], request.GET['max-price']
            )
        ).order_by(order_by)

    contex = {
        'user_request': request.GET['user-request'],
        'user_size': request.GET['user-size'],
        'db_response_items': search_result,
        'page': int(request.GET['page']),
    }
    return render(request, 'html/filter.html', contex)
