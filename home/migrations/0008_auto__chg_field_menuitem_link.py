# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MenuItem.link'
        db.alter_column(u'home_menuitem', 'link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'MenuItem.link'
        raise RuntimeError("Cannot reverse this migration. 'MenuItem.link' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MenuItem.link'
        db.alter_column(u'home_menuitem', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'home.calendaritem': {
            'Meta': {'object_name': 'CalendarItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'new_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 21, 0, 0)'})
        },
        u'home.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'home.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'menus': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'menuitems'", 'symmetrical': 'False', 'to': u"orm['home.Menu']"}),
            'new_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'home.slideritem': {
            'Meta': {'object_name': 'SliderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'img_width': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'new_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'home.widget': {
            'Meta': {'object_name': 'Widget'},
            'contents': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['home']