from django.db import models
from django.template.defaultfilters import slugify


class Contact(models.Model):
    email = models.CharField(max_length=250)
    first_name = models.CharField(max_length=70, blank=True)
    middle_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    organization = models.CharField(max_length=250, blank=True)

    # STATUS FLAGS & CALCULATED FIELDS
    opened_in_six_months = models.IntegerField(blank=True, null=True)
    purged = models.BooleanField(default=False)
    purge_candidate = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email

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

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ContactList, self).save(*args, **kwargs)
    
class ListMembership(models.Model):
    contact = models.ForeignKey(Contact)
    contact_list = models.ForeignKey(ContactList)

#class EmailCampaign (an outreach email sent to potential volunteers/donors)
#class EmailAction (response to outreach emails)
