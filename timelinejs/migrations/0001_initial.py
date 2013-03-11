# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timeline'
        db.create_table(u'timelinejs_timeline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'timelinejs', ['Timeline'])

        # Adding model 'TimelineEvent'
        db.create_table(u'timelinejs_timelineevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Timeline'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prayer.Church'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('asset_media', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'timelinejs', ['TimelineEvent'])

        # Adding model 'TimelineOptions'
        db.create_table(u'timelinejs_timelineoptions', (
            ('timeline', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['timelinejs.Timeline'], unique=True, primary_key=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=10)),
            ('height', self.gf('django.db.models.fields.CharField')(default='600', max_length=10)),
            ('embed_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('start_at_end', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_at_slide', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('start_zoom_adjust', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hash_bookmark', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('font', self.gf('django.db.models.fields.CharField')(default='Bevan-PotanoSans', max_length=50)),
            ('debug', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lang', self.gf('django.db.models.fields.CharField')(default='en', max_length=6)),
            ('maptype', self.gf('django.db.models.fields.CharField')(default='watercolor', max_length=50)),
        ))
        db.send_create_signal(u'timelinejs', ['TimelineOptions'])


    def backwards(self, orm):
        # Deleting model 'Timeline'
        db.delete_table(u'timelinejs_timeline')

        # Deleting model 'TimelineEvent'
        db.delete_table(u'timelinejs_timelineevent')

        # Deleting model 'TimelineOptions'
        db.delete_table(u'timelinejs_timelineoptions')


    models = {
        u'prayer.church': {
            'Meta': {'object_name': 'Church'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'denominations': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'geocode_lat': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'geocode_lng': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'})
        },
        u'timelinejs.timelineevent': {
            'Meta': {'object_name': 'TimelineEvent'},
            'asset_caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'asset_media': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prayer.Church']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timelinejs.Timeline']"})
        },
        u'timelinejs.timelineoptions': {
            'Meta': {'object_name': 'TimelineOptions'},
            'debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'embed_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Bevan-PotanoSans'", 'max_length': '50'}),
            'hash_bookmark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'600'", 'max_length': '10'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'maptype': ('django.db.models.fields.CharField', [], {'default': "'watercolor'", 'max_length': '50'}),
            'start_at_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_at_slide': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_zoom_adjust': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'timeline': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['timelinejs.Timeline']", 'unique': 'True', 'primary_key': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '10'})
        }
    }

    complete_apps = ['timelinejs']