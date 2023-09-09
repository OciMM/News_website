from django.db import models


class Category(models.Model):
    """Categories of app News. Here is categories of these models.
    For example 'Global News'"""
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=120, blank=True, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "Categories"


class Tag(models.Model):
    """Tags of app News. Here is tags of these models.
    For example 'Politic', 'Economic, 'Sport' etc."""
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=120, blank=True, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = 'Теги'
        db_table = "Tags"


class News(models.Model):
    """Model of news. This model will be using for to create a news post."""
    title = models.CharField(max_length=150, verbose_name="Название поста")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    main_image = models.ImageField(upload_to='media/news_images/', verbose_name="Главное изображение поста")
    text = models.TextField(verbose_name="Содержание поста")
    start_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        db_table = "News"
