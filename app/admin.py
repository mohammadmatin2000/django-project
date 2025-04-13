from django.contrib import admin
from app.models import Contact
# ======================================================================================================================
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-empty-'
admin.site.register(Contact, ContactAdmin)
# ======================================================================================================================