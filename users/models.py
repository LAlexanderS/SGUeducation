# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from personal.models import Personal

class User(AbstractUser):
    USER_ROLES = [
        ('employee', 'Сотрудник'),
        ('operator', 'Оператор'),
        ('admin', 'Администратор'),
    ]
    
    role = models.CharField(max_length=10, choices=USER_ROLES, default='employee')
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    id_s = models.ForeignKey(Personal, blank=True, null=True, to_field='ID', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
         return self.username
