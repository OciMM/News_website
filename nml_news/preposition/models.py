from django.db import models


class Category(models.Model):
    """Categories in this website"""
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="url-название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "Category_Preposition"


class PrepositionModel(models.Model):
    """Model which may to use for preposition"""
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Категория")
    text = models.TextField(max_length=2000, blank=True, verbose_name="Текст предложения")
    file = models.FileField(upload_to='preposition_files/', blank=True, null=True, verbose_name="Загрузить файлы")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата предложения")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Идея из предложки"
        verbose_name_plural = "Идеи из предложки"
        db_table = "IdeasFromPreposition"
