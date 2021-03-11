from django.db import models
from django.urls import reverse


class Stoic(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    month = models.ForeignKey('Month', on_delete=models.PROTECT, verbose_name='Месяц')
    views = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('view_stoic', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Высказывание'
        verbose_name_plural = 'Дни'
        ordering = ['id']


class Month(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование месяца')

    def get_absolute_url(self):
        return reverse('month', kwargs={"month_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
        ordering = ['id']
