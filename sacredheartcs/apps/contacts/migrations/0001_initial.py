# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('contacts_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cc_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, db_index=True, blank=True)),
            ('cc_status', self.gf('django.db.models.fields.CharField')(default='', max_length=200, db_index=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('email_type', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=70, blank=True)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=250, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True)),
            ('added_by', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address_line_3', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('us_state_or_ca_province', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=200, blank=True)),
            ('other_state_or_province', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('zip_or_postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('sub_zip_or_postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('custom_field1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field3', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field4', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field5', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field6', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field7', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field8', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field9', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field10', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field11', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field12', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field13', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field14', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('custom_field15', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('opened_in_six_months', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('purged', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('purge_candidate', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        ))
        db.send_create_signal('contacts', ['Contact'])

        # Adding model 'ContactList'
        db.create_table('contacts_contactlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cc_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contacts', ['ContactList'])

        # Adding unique constraint on 'ContactList', fields ['name']
        db.create_unique('contacts_contactlist', ['name'])

        # Adding model 'ListMembership'
        db.create_table('contacts_listmembership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('contact_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactList'])),
        ))
        db.send_create_signal('contacts', ['ListMembership'])

        # Adding unique constraint on 'ListMembership', fields ['contact', 'contact_list']
        db.create_unique('contacts_listmembership', ['contact_id', 'contact_list_id'])

        # Adding model 'EmailAction'
        db.create_table('contacts_emailaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('action_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('contacts', ['EmailAction'])

        # Adding unique constraint on 'EmailAction', fields ['contact', 'action', 'action_date']
        db.create_unique('contacts_emailaction', ['contact_id', 'action', 'action_date'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'EmailAction', fields ['contact', 'action', 'action_date']
        db.delete_unique('contacts_emailaction', ['contact_id', 'action', 'action_date'])

        # Removing unique constraint on 'ListMembership', fields ['contact', 'contact_list']
        db.delete_unique('contacts_listmembership', ['contact_id', 'contact_list_id'])

        # Removing unique constraint on 'ContactList', fields ['name']
        db.delete_unique('contacts_contactlist', ['name'])

        # Deleting model 'Contact'
        db.delete_table('contacts_contact')

        # Deleting model 'ContactList'
        db.delete_table('contacts_contactlist')

        # Deleting model 'ListMembership'
        db.delete_table('contacts_listmembership')

        # Deleting model 'EmailAction'
        db.delete_table('contacts_emailaction')


    models = {
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'added_by': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cc_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cc_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'db_index': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'custom_field1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field10': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field11': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field12': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field13': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field14': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field15': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field3': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field4': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field5': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field6': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field7': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field8': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'custom_field9': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'email_type': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '70', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'opened_in_six_months': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'other_state_or_province': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'purge_candidate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'purged': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'sub_zip_or_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'us_state_or_ca_province': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'zip_or_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'contacts.contactlist': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name',),)", 'object_name': 'ContactList'},
            'cc_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Contact']", 'through': "orm['contacts.ListMembership']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'})
        },
        'contacts.emailaction': {
            'Meta': {'unique_together': "(('contact', 'action', 'action_date'),)", 'object_name': 'EmailAction'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'action_date': ('django.db.models.fields.DateField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contacts.listmembership': {
            'Meta': {'ordering': "['contact_list']", 'unique_together': "(('contact', 'contact_list'),)", 'object_name': 'ListMembership'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactList']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']
