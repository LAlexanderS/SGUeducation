from django.db import models
from passengers.models import Passengers
from metro.models import Station


class Application(models.Model):
    
    id = models.AutoField(primary_key=True)
    CAT_CHOICES = [
        ('ИЗТ', 'Инвалид по зрению'),
        ('ИЗ', 'Инвалид по зрению с остаточным зрением'),
        ('ИС', 'Инвалид по слуху'),
        ('ИК', 'Инвалид колясочник'),
        ('ИО', 'Инвалид опорник'),
        ('ДИ', 'Ребенок инвалид'),
        ('ПЛ', 'Пожилой человек'),
        ('РД', 'Родители с детьми'),
        ('РДК', 'Родители с детскими колясками'),
        ('ОГД', 'Организованные группы детей'),
        ('ОВ', 'Временно маломобильные'),
        ('ИУ', 'Люди с ментальной инвалидностью'),
    ]
    SMENA_CHOICES = [
        ('Не подтверждена', 'Не подтверждена'),
        ('В рассмотрении', 'В рассмотрении'),
        ('Принята', 'Принята'),
        ('Инспектор выехал', 'Инспектор выехал'),
        ('Инспектор на месте', 'Инспектор на месте'),
        ('Поездка', 'Поездка'),
        ('Заявка закончена', 'Заявка закончена'),
        ('Выявление', 'Выявление'),
        ('Лист Ожидания', 'Лист Ожидания'),
        ('Отмена', 'Отмена'),
        ('Отказ', 'Отказ'),
        ('Пассажир опаздывает', 'Пассажир опаздывает'),
        ('Инспектор опаздывает', 'Инспектор опаздывает'),
    ]
    id_pas = models.ForeignKey(Passengers, on_delete=models.CASCADE, verbose_name='Сотрудник', blank=True, null=True)
    datetime = models.DateTimeField(verbose_name='Дата и время начала заявки')
    tpz = models.DateTimeField(verbose_name='Дата и время окончания заявки')
    # time3 = models.TimeField(verbose_name='Время встречи с пассажиром')
    # time4 = models.TimeField(verbose_name='Время исполнения заявки')
    tpz = models.DateTimeField(verbose_name='Время регистрации заявки')
    # INSP_SEX_M = models.IntegerField(verbose_name='Количество сотрудников мужчин')
    # INSP_SEX_F = models.IntegerField(verbose_name='Количество сотрудников женщин')
    # TIME_OVER = models.TimeField(verbose_name='Время окончания заявки', blank=True, null=True)
    # cat_pas = models.CharField(max_length=50, verbose_name='Категория пассажиров',blank=True, null=True,choices= CAT_CHOICES)
    # id_st1 = models.ForeignKey(Station, related_name='departure_station', on_delete=models.CASCADE, verbose_name='Станция отправления',to_field='id')
    # id_st2 = models.ForeignKey(Station, related_name='arrival_station', on_delete=models.CASCADE, verbose_name='Станция прибытия',to_field='id')
   # id_st1 = models.CharField(max_length=100,verbose_name='ID станции отправления')
    #id_st2 = models.CharField(max_length=100,verbose_name='ID станции прибытия')
    # status = models.CharField(max_length=50, verbose_name='Текущий статус заявки',blank=True, null=True,choices= SMENA_CHOICES)
    # vokzal = models.BooleanField(verbose_name='Необходимость встретить с воказала', blank=True, null=True)
    dop_inf = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    # bag_s = models.BooleanField(verbose_name='Наличие багажа', blank=True, null=True)
    # pass_count = models.IntegerField(verbose_name='Количество пассажиров',blank=True, null=True)
    # method_p = models.CharField(max_length=50, verbose_name='Метод приёма заявки',blank=True, null=True)

    class Meta:
        db_table = 'Application'
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.id}'

# class ApplicationTransfer(models.Model):
#     id_adit = models.AutoField(primary_key=True)
#    # id_bid = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Заявка',blank =True,null=True,to_field='id',related_name= 'bid')
#     id_bid = models.ForeignKey(Application, related_name='ID_Application', on_delete=models.CASCADE, verbose_name='ID Заявки',to_field='id')
#     time_edit = models.DateTimeField(verbose_name='Время изменения',blank=True, null=True)
#    # time_s = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Изначальное время заявки', to_field='time3', related_name='initial_transfers')
#     time_s = models.TimeField(verbose_name='Начальное время',blank=True, null=True)
#     time_f = models.TimeField(verbose_name='Желаемое время',blank=True, null=True)
#     date_time = models.DateTimeField(verbose_name='Время неявки /Отмены',blank=True, null=True)

#     class Meta:
#         db_table = 'ApplicationTransfer'
#         verbose_name = 'Перенос заявки'
#         verbose_name_plural = 'Переносы заявок'
   
#     def __str__(self):
#         return f'Перенос заявки {self.id_adit}'
    
    


# Create your models here.
