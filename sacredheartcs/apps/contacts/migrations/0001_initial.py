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
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('opened_in_six_months', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('purged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('purge_candidate', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contacts', ['Contact'])

        # Adding model 'ContactList'
        db.create_table('contacts_contactlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contacts', ['ContactList'])

        # Adding model 'ListMembership'
        db.create_table('contacts_listmembership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('contact_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactList'])),
        ))
        db.send_create_signal('contacts', ['ListMembership'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('contacts_contact')

        # Deleting model 'ContactList'
        db.delete_table('contacts_contactlist')

        # Deleting model 'ListMembership'
        db.delete_table('contacts_listmembership')


    models = {
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'opened_in_six_months': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'purge_candidate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'purged': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'contacts.contactlist': {
            'Meta': {'object_name': 'ContactList'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Contact']", 'through': "orm['contacts.ListMembership']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'})
        },
        'contacts.listmembership': {
            'Meta': {'object_name': 'ListMembership'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']"}),
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactList']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']
