# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Thing.widget'
        db.alter_column('mainapp_thing', 'widget', self.gf('django.db.models.fields.TextField')(max_length=10000))

        # Changing field 'Thing.mini_desc'
        db.alter_column('mainapp_thing', 'mini_desc', self.gf('django.db.models.fields.TextField')(max_length=3000))


    def backwards(self, orm):
        
        # Changing field 'Thing.widget'
        db.alter_column('mainapp_thing', 'widget', self.gf('django.db.models.fields.CharField')(max_length=10000))

        # Changing field 'Thing.mini_desc'
        db.alter_column('mainapp_thing', 'mini_desc', self.gf('django.db.models.fields.CharField')(max_length=3000))


    models = {
        'mainapp.tag': {
            'Meta': {'object_name': 'Tag'},
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'mainapp.thing': {
            'Meta': {'object_name': 'Thing'},
            'big_image': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {}),
            'mini_desc': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainapp.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'widget': ('django.db.models.fields.TextField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['mainapp']
