# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table(u'customer_area_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blog_author', null=True, to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'customer_area', ['Blog'])

        # Adding model 'Comment'
        db.create_table(u'customer_area_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment_author', to=orm['auth.User'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'customer_area', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table(u'customer_area_blog')

        # Deleting model 'Comment'
        db.delete_table(u'customer_area_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'customer_area.blog': {
            'Meta': {'object_name': 'Blog'},
            'article': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blog_author'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'customer_area.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_author'", 'to': u"orm['auth.User']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'customer_area.family': {
            'Meta': {'object_name': 'Family'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True'}),
            'father_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'father_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'full_time_children': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_charge': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mother_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'mother_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'nanny': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family_nanny'", 'null': 'True', 'to': u"orm['customer_area.Nanny']"}),
            'part_time_children': ('django.db.models.fields.IntegerField', [], {}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family_user'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'})
        },
        u'customer_area.nanny': {
            'Meta': {'object_name': 'Nanny'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nanny_user'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'weekly_pay': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True'})
        }
    }

    complete_apps = ['customer_area']