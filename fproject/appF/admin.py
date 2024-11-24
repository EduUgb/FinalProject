from django.contrib import admin
from .models import Reserv
# Register your models here.
#admin.site.register(Reserv)


class ReservAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'fecha', 'hora', 'mesa', 'numPersonas')


admin.site.register(Reserv, ReservAdmin)
