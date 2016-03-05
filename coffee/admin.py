from django.contrib import admin

from .models import Order
from .models import Drink

class DrinkInLine(admin.TabularInline):
	model = Drink
	extra = 4

class OrderAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields' : ['description_text']}),
		('Date Information',	{'fields' : ['date']}),
	]
	inlines = [DrinkInLine]
	list_display = ('date', 'description_text', 'was_recent')
	list_filter = ['date']
	searh_fields = ['description_text']

admin.site.register(Order, OrderAdmin)
