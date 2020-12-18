from django.db import models
from django.urls import reverse


def product_image_directory_path(instance, filename):
    # instance - экземпляр модели ProductImage
    # filename - имя сохраняемого файла
    # Изображение будет сохранено в MEDIA_ROOT/product_<id>/<filename>
    return 'product_{0}/{1}'.format(instance.product.id, filename)


class BasicInfo(models.Model):
    email = models.EmailField(verbose_name='Почта', default='test@mail')
    phone = models.CharField(verbose_name='Номер телефона', default='+79994566231', max_length=20)
    address = models.CharField(verbose_name='адрес', default='Москва', max_length=200)
    about = models.TextField(verbose_name='О нас', default='')


class Products(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=100, db_index=True)
    slug = models.SlugField(verbose_name='Уникальная ссылка на товар', max_length=200, db_index=True)
    title = models.CharField(verbose_name='Краткое описание', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name='Опубликовать', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товаров'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])


class ProductImage(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to=product_image_directory_path, blank=True)
    name = models.CharField(verbose_name='Название продукта', max_length=100, db_index=True)
    product = models.ForeignKey(Products, verbose_name='Продукт', related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return 'Фотографии'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Reviews(models.Model):
    """Отзывы"""

    name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField(verbose_name='Почта')
    title = models.CharField(verbose_name='Тема', max_length=200)
    text = models.TextField("Сообщение", max_length=5000)
    product = models.ForeignKey(Products, verbose_name="Продукт", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Дата создания отзыва", auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        db_table = 'Reviews'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Reservation(models.Model):
    """
    Форма заказа товара
    """
    product = models.ForeignKey(Products, verbose_name='Продукт', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=200)
    email = models.EmailField(verbose_name='Email', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    available = models.BooleanField(default=False, verbose_name='Ответ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
