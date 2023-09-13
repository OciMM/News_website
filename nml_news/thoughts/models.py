from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Categories of app Thoughts. Here is categories of these models.
    For example 'Economic, Sociology, etc'"""
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=120, blank=True, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "Categories_thoughts"


class Tag(models.Model):
    """Tags of app Thoughts. Here is tags of these models.
    For example 'Politic', 'Economic, 'Sport' etc."""
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=120, blank=True, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = 'Теги'
        db_table = "Tags_thoughts"


class Thoughts(models.Model):
    """Model of thoughts. This model will be using for to create a thoughts post."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=150, verbose_name="Название поста")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    main_image = models.ImageField(upload_to='media/news_images/', verbose_name="Главное изображение поста")
    text = models.TextField(verbose_name="Содержание поста")
    start_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name="url-название")
    draft = models.BooleanField(default=False, verbose_name="Черновик")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мысль"
        verbose_name_plural = "Мысли"
        db_table = "Thoughts"
