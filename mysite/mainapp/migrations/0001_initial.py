# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tag'
        db.create_table('mainapp_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('human_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('mainapp', ['Tag'])

        # Adding model 'Thing'
        db.create_table('mainapp_thing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=3000)),
            ('mini_desc', self.gf('django.db.models.fields.TextField')(max_length=3000)),
            ('widget', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('big_image', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('karma', self.gf('django.db.models.fields.IntegerField')(default=1, null=True)),
            ('hide', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mainapp', ['Thing'])

        # Adding M2M table for field tags on 'Thing'
        db.create_table('mainapp_thing_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('thing', models.ForeignKey(orm['mainapp.thing'], null=False)),
            ('tag', models.ForeignKey(orm['mainapp.tag'], null=False))
        ))
        db.create_unique('mainapp_thing_tags', ['thing_id', 'tag_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tag'
        db.delete_table('mainapp_tag')

        # Deleting model 'Thing'
        db.delete_table('mainapp_thing')

        # Removing M2M table for field tags on 'Thing'
        db.delete_table('mainapp_thing_tags')


    models = {
        'mainapp.tag': {
            'Meta': {'object_name': 'Tag'},
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'mainapp.thing': {
            'Meta': {'object_name': 'Thing'},
            'big_image': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'mini_desc': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainapp.Tag']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'widget': ('django.db.models.fields.TextField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['mainapp']
