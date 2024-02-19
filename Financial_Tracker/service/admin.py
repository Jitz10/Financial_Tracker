from django.contrib import admin

from service.models import dta, service ,incoming_data,Transaction
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

class dtaAdmin(admin.ModelAdmin):
    list_display = ('cost','cat','date_and_time')
class incoming_data_admin(admin.ModelAdmin):
    list_display = ('type','category','description','amount','recurring','term','endDate')
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'category', 'description', 'amount', 'recurring', 'term', 'end_date')
    search_fields = ('type', 'name', 'category', 'description')
    list_filter = ('recurring', 'term', 'end_date')

admin.site.register(service,ServiceAdmin)
admin.site.register(dta,dtaAdmin)
admin.site.register(incoming_data,incoming_data_admin)
admin.site.register(Transaction,TransactionAdmin)
# Register your models here.
