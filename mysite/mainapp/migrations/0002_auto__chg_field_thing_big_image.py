# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Thing.big_image'
        db.alter_column('mainapp_thing', 'big_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Thing.big_image'
        db.alter_column('mainapp_thing', 'big_image', self.gf('django.db.models.fields.CharField')(max_length=300))


    models = {
        'mainapp.tag': {
            'Meta': {'object_name': 'Tag'},
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'mainapp.thing': {
            'Meta': {'object_name': 'Thing'},
            'big_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {}),
            'mini_desc': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainapp.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'widget': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['mainapp']
