from django.contrib import admin
from .models import Passengers

class PassengersAdmin(admin.ModelAdmin):
    list_display = ('id_pas', 'fio_p', 'tep_p',)
    list_display_links = ('id_pas', 'fio_p')
    search_fields = ('fio_p', 'tep_p')

    def eks_display(self, obj):
        return 'Да' if obj.eks else 'Нет'
    eks_display.short_description = 'Наличие кардиостимулятора'

admin.site.register(Passengers, PassengersAdmin)
