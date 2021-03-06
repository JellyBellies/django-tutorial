from django.contrib import admin
from addressbook.models import Record, County, City, Title

class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', { 'fields': ['title', 'firstname', 'surname']}),
        ('Address', { 'fields': ['address_line_1', 'address_line_2', 'address_line_3', 'city', 'county', 'postcode']}),
]
    list_display = ('get_name', 'get_address')
    search_fields = ['firstname', 'surname']

admin.site.register(Record, RecordAdmin)

admin.site.register(County)
admin.site.register(City)
admin.site.register(Title)

# Register your models here.
