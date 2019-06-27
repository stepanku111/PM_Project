from django.db import models


class BaseItem(models.Model):
    name = models.TextField(verbose_name="Название товара", blank=True, default='')
    picture = models.TextField(verbose_name="Ссылка на изображение товра", blank=True, default='')
    old_price = models.DecimalField(verbose_name='Цена без скидки', max_digits=17, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=17, decimal_places=2, default=0)
    description = models.TextField(verbose_name="Описание товара", blank=True, default='')
    url = models.TextField(verbose_name="Ссылка на товар", blank=True, default='')
    discount = models.PositiveIntegerField(verbose_name='Процент скидки', default=0, )
    color = models.TextField(verbose_name="Цвет", blank=True, default='')
    size = models.TextField(verbose_name="Размеры", blank=True, default='')
    sex = models.TextField(verbose_name="Пол", blank=True, default='')
    material = models.TextField(verbose_name="Материал", blank=True, default='')
    season = models.TextField(verbose_name="Сизон", blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.name)


class Boot(BaseItem):
    class Meta:
        verbose_name = 'Boot'


class Accessory(BaseItem):
    class Meta:
        verbose_name = 'Accessory'


class Hat(BaseItem):
    class Meta:
        verbose_name = 'Hat'


class LowerOuter(BaseItem):
    class Meta:
        verbose_name = 'LowerOuter'


class UnderPants(BaseItem):
    class Meta:
        verbose_name = 'UnderPants'


class Pants(BaseItem):
    class Meta:
        verbose_name = 'Pants'


class OuterWear(BaseItem):
    class Meta:
        verbose_name = 'OuterWear'
