from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'datetime', 'tpz', 'dop_inf'
    )
    list_display_links = ('id',)
    list_filter = ('datetime',)
    search_fields = ('id_pas__fio_p',)

# class ApplicationTransferAdmin(admin.ModelAdmin):
#     list_display = ('id_bid', 'time_edit','time_f')


    # def get_time3(self, obj):
        # if obj.time_s:
            # return obj.time_s.time3
        # return None
    # get_time3.short_description = 'Изначальное время заявки'


admin.site.register(Application, ApplicationAdmin)
# admin.site.register(ApplicationTransfer, ApplicationTransferAdmin)
