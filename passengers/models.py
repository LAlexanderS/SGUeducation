from django.db import models

class Passengers(models.Model):
    
    id_pas = models.AutoField(primary_key=True, verbose_name = 'ID')
    fio_p = models.CharField(max_length=255, verbose_name = 'Название')
    tep_p = models.CharField(max_length=50, verbose_name = 'Организация')

    dop_inf = models.TextField(blank=True, null=True,verbose_name = 'Дополнительная информация')


  
    class Meta:
        db_table = 'Passengers'
        verbose_name = 'Пассажира'
        verbose_name_plural = 'Пассажиры'
    
    def __str__(self):
        return self.fio_p
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.category = "Пассажиры"	
    #     super(Passengers, self).save(*args, **kwargs)
