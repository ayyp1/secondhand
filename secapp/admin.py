from django.contrib import admin
from .models import Bike



admin.site.site_header = "second hand"
admin.site.site_title = "second hand"
admin.site.index_title="Marketplace for shand"

class BikeAdmin(admin.ModelAdmin):
    list_display = ('name' ,'bikenum', 'desc')
    search_fields = ('name',)

    def set_sold(self,request,queryset):
        queryset.update(desc='sold')

    actions = ('set_sold',)

admin.site.register(Bike,BikeAdmin)
# Register your models here.
 