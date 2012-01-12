from django.contrib import admin

from models import Contact, ContactList, ListMembership


class ListMembershipInline(admin.TabularInline):
    model = ListMembership

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ListMembershipInline,
    ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactList)
admin.site.register(ListMembership)
