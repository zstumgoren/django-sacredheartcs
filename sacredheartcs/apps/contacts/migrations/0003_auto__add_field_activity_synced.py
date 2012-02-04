# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Activity.synced'
        db.add_column('contacts_activity', 'synced', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Activity.synced'
        db.delete_column('contacts_activity', 'synced')


    models = {
        'contacts.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cc_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'errors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_time': ('django.db.models.fields.DateTimeField', [], {}),
            'run_finish_time': ('django.db.models.fields.DateTimeField', [], {}),
            'run_start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'synced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_count': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'added_by': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
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
            'needs_update': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
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
