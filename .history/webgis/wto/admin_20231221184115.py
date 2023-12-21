from django.contrib import admin
from .models import Country, ProductSector, Book, BookInstance

# Register your models here.
admin.site.register(Country)
admin.site.register(ProductSector)
admin.site.register(TradeYearData)
admin.site.register(TradeQuarterData)
admin.site.register(TradeMonthData)
admin.site.register(TradeIndexData)