from django.db import models
from django.urls import reverse
import datetime
today = datetime.datetime.today()


TITLE_CHOICES = [
    ('Неактивна ❌', 'Неактивна ❌'),
    ('Активна ✅', 'Активна ✅'),
    ('Просрочена', 'Просрочена'),
]


class CreditCards(models.Model):
    seria = models.TextField(
        verbose_name='Серия'
    )
    number = models.TextField(
        verbose_name='Номер'
    )
    data_vipusk = models.TextField(
        verbose_name='Дата Выпуска'
    )
    data_okonchania = models.TextField(
        verbose_name='Дата окончания'
    )
    data_ispolzovania = models.TextField(
        verbose_name='Дата использования'
    )
    summa = models.TextField(
        verbose_name='Сумма'
    )
    statuscard = models.CharField(
        verbose_name='Статус Карты',
        choices = TITLE_CHOICES,
        max_length = 70,
    )


    def __str__(self):
        return f'#{self.seria} {self.number} {self.data_vipusk} {self.data_okonchania} {self.data_ispolzovania} {self.summa} {self.statuscard}'

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class HistoryCard(models.Model):
    id_card = models.PositiveIntegerField(
        verbose_name='ID карты'
    )
    who_buy = models.TextField(
        verbose_name='Кто купил'
    )
    what_buy = models.TextField(
        verbose_name='Что купил'
    )
    price_tovar = models.TextField(
        verbose_name='Цена Товара'
    )



    def __str__(self):
        return f'#{self.id_card} {self.who_buy} {self.what_buy} {self.price_tovar}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'