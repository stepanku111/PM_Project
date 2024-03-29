# Generated by Django 2.2.2 on 2019-06-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'Accessory',
            },
        ),
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'Hat',
            },
        ),
        migrations.CreateModel(
            name='LowerOuter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'LowerOuter',
            },
        ),
        migrations.CreateModel(
            name='OuterWear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'OuterWear',
            },
        ),
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'Pants',
            },
        ),
        migrations.CreateModel(
            name='UnderPants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Название товара')),
                ('picture', models.TextField(blank=True, default='', verbose_name='Ссылка на изображение товра')),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена без скидки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=17, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание товара')),
                ('url', models.TextField(blank=True, default='', verbose_name='Ссылка на товар')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Процент скидки')),
                ('color', models.TextField(blank=True, default='', verbose_name='Цвет')),
                ('size', models.TextField(blank=True, default='', verbose_name='Размеры')),
                ('sex', models.TextField(blank=True, default='', verbose_name='Пол')),
                ('material', models.TextField(blank=True, default='', verbose_name='Материал')),
                ('season', models.TextField(blank=True, default='', verbose_name='Сизон')),
            ],
            options={
                'verbose_name': 'UnderPants',
            },
        ),
    ]
