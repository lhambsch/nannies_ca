# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Family'
        db.create_table(u'customer_area_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mother', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('father', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('full_time_children', self.gf('django.db.models.fields.IntegerField')()),
            ('part_time_children', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'customer_area', ['Family'])


    def backwards(self, orm):
        # Deleting model 'Family'
        db.delete_table(u'customer_area_family')


    models = {
        u'customer_area.family': {
            'Meta': {'object_name': 'Family'},
            'father': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'full_time_children': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'part_time_children': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['customer_area']