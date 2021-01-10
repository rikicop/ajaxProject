from django.contrib import admin
from .models import Contact,Sum


admin.site.register(Sum)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','cargo','email','message')
    list_filter = ('message',)
    search_fields = ('name',)

    def get_ordering(self,request):
        if request.user.is_superuser:
            return('name','cargo')
        return('name',)

admin.site.register(Contact, ContactAdmin)
