from django.db import models
from django.template.defaultfilters import slugify


class Contact(models.Model):
    email_address = models.CharField(max_length=250, unique=True)
    email_type = models.CharField(max_length=250)
    first_name = models.CharField(max_length=70, blank=True)
    middle_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True, db_index=True)
    job_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=250, blank=True, db_index=True)
    date_added = models.DateTimeField(blank=True, null=True, db_index=True)
    added_by = models.CharField(max_length=250, blank=True)
    work_phone = models.CharField(max_length=12, blank=True)
    home_phone = models.CharField(max_length=12, blank=True)
    address_line_1 = models.CharField(max_length=200, blank=True)
    address_line_2 = models.CharField(max_length=200, blank=True)
    address_line_3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    us_state_or_ca_province = models.CharField(max_length=200, blank=True, db_index=True)
    other_state_or_province = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    zip_or_postal_code = models.CharField(max_length=10, blank=True)
    sub_zip_or_postal_code = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)

    # STATUS FLAGS & CALCULATED FIELDS
    opened_in_six_months = models.IntegerField(blank=True, null=True, db_index=True,
                                               help_text='Number of times this contact opened email in last 6 months. Updated daily.')
    purged = models.BooleanField(default=False, db_index=True)
    purge_candidate = models.BooleanField(default=False, db_index=True)


    def __unicode__(self):
        return self.email_address

class ContactList(models.Model):
    """
    A Constant Contacts "list" is used to group contacts together.
    For example, all volunteers for a Thanksgiving fundraiser might be
    assigned to "List: Thanksgiving".

    A contact can be assigned to one or more lists.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    contacts = models.ManyToManyField(Contact, through='ListMembership', help_text='Constant Contacts lists this person is assigned to')

    class Meta:
        unique_together = ('name',)
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ContactList, self).save(*args, **kwargs)
    
class ListMembership(models.Model):
    contact = models.ForeignKey(Contact)
    contact_list = models.ForeignKey(ContactList)

    class Meta:
        unique_together = ('contact', 'contact_list')
        ordering = ['contact_list']

    def __unicode__(self):
        return '%s (%s)' % (self.contact, self.contact_list)

#class EmailCampaign (an outreach email sent to potential volunteers/donors)
#class EmailAction (response to outreach emails)
