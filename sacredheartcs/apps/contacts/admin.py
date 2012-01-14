from django.contrib import admin

from models import Contact, ContactList, ListMembership


class ListMembershipAdmin(admin.ModelAdmin):
    list_filter = ('contact_list',)

class ListMembershipInline(admin.TabularInline):
    model = ListMembership
    extra = 0

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ListMembershipInline,
    ]
    list_display = ('email_address','company_name', 'purged', 'purge_candidate','opened_in_six_months') 
    list_filter = ('opened_in_six_months', 'purged', 'purge_candidate')

    #field_set  status (purged, purge_candidate, etc.), info (name, address, etc.), meta (date_added, added_by)
    fieldsets = (
        (None, {
            'fields':(('email_address', 'email_type'),)
        }),
        ('Status', {
            'classes':('collapse',),
            'fields': (('purged', 'purge_candidate', 'opened_in_six_months'),),
        }),
        ('Contact Info', {
            'classes':('collapse',),
            'fields': (
                    ('first_name', 'middle_name', 'last_name'),
                    ('company_name', 'job_title'),
                    ('work_phone', 'home_phone'),
                    'address_line_1',
                    'address_line_2',
                    'address_line_3',
                    'city',
                    ('us_state_or_ca_province', 'other_state_or_province'),
                    ('zip_or_postal_code', 'sub_zip_or_postal_code'),
                    'country',
            ),
        }),
        ('Meta', {
            'classes':('collapse',),
            'fields':('date_added', 'added_by'),
        }),

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactList)
admin.site.register(ListMembership, ListMembershipAdmin)
