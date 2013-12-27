# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company._hash'
        db.add_column(u'ine_company', '_hash',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Company._hash'
        db.delete_column(u'ine_company', '_hash')


    models = {
        u'ine.company': {
            'Meta': {'object_name': 'Company'},
            '_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            '_type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ine.resume': {
            'Meta': {'object_name': 'Resume'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2016', 'max_length': '4'})
        },
        u'ine.resumebook': {
            'Meta': {'object_name': 'ResumeBook'},
            '_type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'book': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2016', 'max_length': '4'})
        }
    }

    complete_apps = ['ine']