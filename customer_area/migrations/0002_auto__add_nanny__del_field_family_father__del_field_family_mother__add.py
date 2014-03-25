# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nanny'
        db.create_table(u'customer_area_nanny', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=14, null=True)),
            ('phone1', self.gf('django.db.models.fields.CharField')(max_length=14, null=True)),
            ('phone2', self.gf('django.db.models.fields.CharField')(max_length=14, null=True)),
            ('phone3', self.gf('django.db.models.fields.CharField')(max_length=14, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True)),
            ('weekly_pay', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='nanny_user', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'customer_area', ['Nanny'])

        # Deleting field 'Family.father'
        db.delete_column(u'customer_area_family', 'father')

        # Deleting field 'Family.mother'
        db.delete_column(u'customer_area_family', 'mother')

        # Adding field 'Family.mother_first_name'
        db.add_column(u'customer_area_family', 'mother_first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Family.mother_last_name'
        db.add_column(u'customer_area_family', 'mother_last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Family.father_first_name'
        db.add_column(u'customer_area_family', 'father_first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Family.father_last_name'
        db.add_column(u'customer_area_family', 'father_last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Family.address1'
        db.add_column(u'customer_area_family', 'address1',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Family.address2'
        db.add_column(u'customer_area_family', 'address2',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Family.city'
        db.add_column(u'customer_area_family', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Family.state'
        db.add_column(u'customer_area_family', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'Family.zip'
        db.add_column(u'customer_area_family', 'zip',
                      self.gf('django.db.models.fields.CharField')(max_length=14, null=True),
                      keep_default=False)

        # Adding field 'Family.phone1'
        db.add_column(u'customer_area_family', 'phone1',
                      self.gf('django.db.models.fields.CharField')(max_length=14, null=True),
                      keep_default=False)

        # Adding field 'Family.phone2'
        db.add_column(u'customer_area_family', 'phone2',
                      self.gf('django.db.models.fields.CharField')(max_length=14, null=True),
                      keep_default=False)

        # Adding field 'Family.phone3'
        db.add_column(u'customer_area_family', 'phone3',
                      self.gf('django.db.models.fields.CharField')(max_length=14, null=True),
                      keep_default=False)

        # Adding field 'Family.email'
        db.add_column(u'customer_area_family', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=254, null=True),
                      keep_default=False)

        # Adding field 'Family.created_on'
        db.add_column(u'customer_area_family', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 23, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Family.start_date'
        db.add_column(u'customer_area_family', 'start_date',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Family.monthly_charge'
        db.add_column(u'customer_area_family', 'monthly_charge',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'Family.nanny'
        db.add_column(u'customer_area_family', 'nanny',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='family_nanny', null=True, to=orm['customer_area.Nanny']),
                      keep_default=False)

        # Adding field 'Family.user'
        db.add_column(u'customer_area_family', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='family_user', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Nanny'
        db.delete_table(u'customer_area_nanny')

        # Adding field 'Family.father'
        db.add_column(u'customer_area_family', 'father',
                      self.gf('django.db.models.fields.CharField')(default='father', max_length=100),
                      keep_default=False)

        # Adding field 'Family.mother'
        db.add_column(u'customer_area_family', 'mother',
                      self.gf('django.db.models.fields.CharField')(default='mother', max_length=100),
                      keep_default=False)

        # Deleting field 'Family.mother_first_name'
        db.delete_column(u'customer_area_family', 'mother_first_name')

        # Deleting field 'Family.mother_last_name'
        db.delete_column(u'customer_area_family', 'mother_last_name')

        # Deleting field 'Family.father_first_name'
        db.delete_column(u'customer_area_family', 'father_first_name')

        # Deleting field 'Family.father_last_name'
        db.delete_column(u'customer_area_family', 'father_last_name')

        # Deleting field 'Family.address1'
        db.delete_column(u'customer_area_family', 'address1')

        # Deleting field 'Family.address2'
        db.delete_column(u'customer_area_family', 'address2')

        # Deleting field 'Family.city'
        db.delete_column(u'customer_area_family', 'city')

        # Deleting field 'Family.state'
        db.delete_column(u'customer_area_family', 'state')

        # Deleting field 'Family.zip'
        db.delete_column(u'customer_area_family', 'zip')

        # Deleting field 'Family.phone1'
        db.delete_column(u'customer_area_family', 'phone1')

        # Deleting field 'Family.phone2'
        db.delete_column(u'customer_area_family', 'phone2')

        # Deleting field 'Family.phone3'
        db.delete_column(u'customer_area_family', 'phone3')

        # Deleting field 'Family.email'
        db.delete_column(u'customer_area_family', 'email')

        # Deleting field 'Family.created_on'
        db.delete_column(u'customer_area_family', 'created_on')

        # Deleting field 'Family.start_date'
        db.delete_column(u'customer_area_family', 'start_date')

        # Deleting field 'Family.monthly_charge'
        db.delete_column(u'customer_area_family', 'monthly_charge')

        # Deleting field 'Family.nanny'
        db.delete_column(u'customer_area_family', 'nanny_id')

        # Deleting field 'Family.user'
        db.delete_column(u'customer_area_family', 'user_id')


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