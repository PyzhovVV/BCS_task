from django.db import models
from django.urls import reverse


class Translation(models.Model):
    transaction_id = models.CharField(max_length=255, default='some id', verbose_name='ID транзакции')
    description = models.TextField(default='some description', verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.transaction_id

    def get_absolute_url(self):
        return reverse('description', kwargs={'transaction_id': self.pk})

    class Meta:
        verbose_name = 'Список транзакций'
        verbose_name_plural = 'Список транзакций'
        ordering = ['-time_create']
