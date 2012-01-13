from django.db import models
from django.template.defaultfilters import slugify


class Contact(models.Model):
    email_address = models.CharField(max_length=250)
    email_type = models.CharField(max_length=250)
    first_name = models.CharField(max_length=70, blank=True)
    middle_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(blank=True, null=True)
    added_by = models.CharField(max_length=250, blank=True)
    work_phone = models.CharField(max_length=12, blank=True)
    home_phone = models.CharField(max_length=12, blank=True)
    address_line_1 = models.CharField(max_length=200, blank=True)
    address_line_2 = models.CharField(max_length=200, blank=True)
    address_line_3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    us_state_or_ca_province = models.CharField(max_length=200, blank=True)
    other_state_or_province = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    zip_or_postal_code = models.CharField(max_length=10, blank=True)
    sub_zip_or_postal_code = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)

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


"""
Email Address,
Email Type,
List: General Interest,
List: Donors,
List: Volunteers,
List: staff,
List: Schools,
List: Service/Social Orgs,
List: 2010 holiday volunteers,
List: LMV Master List,
List: silicon valley volunteer 6-25/26,
List: Pack-a-Back volunteers 2010-11,i
List: 2011 Holiday volunteers,
List: master,
List: Microsoft Store 12-29-11,
List: Student Conference 12-29-11,
List: Saturday Volunteers 1/7/12,
Date Added,
Added By,
First Name,
Middle Name,
Last Name,
Job Title,
Company Name,
Work Phone,
Home Phone,
Address Line 1,
Address Line 2,
Address Line 3,
City,
US State/CA Province,
Other State/Province,
Country,
Zip/Postal Code,
Sub Zip/Postal Code,
Notes,
Custom field 1,
Custom field 2,
Custom field 3,
Custom field 4,
Custom field 5,
Custom field 6,
Custom field 7,
Custom field 8,
Custom field 9,
Custom field 10,
Custom field 11,
Custom field 12,
Custom field 13,
Custom field 14,
Custom field 15
"""
