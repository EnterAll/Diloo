# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Critic'
        db.create_table(u'app_critic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Critic'])

        # Adding M2M table for field readers on 'Critic'
        m2m_table_name = db.shorten_name(u'app_critic_readers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_critic', models.ForeignKey(orm[u'app.critic'], null=False)),
            ('to_critic', models.ForeignKey(orm[u'app.critic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_critic_id', 'to_critic_id'])

        # Adding M2M table for field to_read on 'Critic'
        m2m_table_name = db.shorten_name(u'app_critic_to_read')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_critic', models.ForeignKey(orm[u'app.critic'], null=False)),
            ('to_critic', models.ForeignKey(orm[u'app.critic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_critic_id', 'to_critic_id'])

        # Adding model 'Category'
        db.create_table(u'app_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Category'])

        # Adding model 'Topic'
        db.create_table(u'app_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Topic'])

        # Adding model 'Score'
        db.create_table(u'app_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('critic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Critic'])),
            ('avg', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Score'])

        # Adding model 'Review'
        db.create_table(u'app_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('critic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Critic'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Category'])),
            ('pre_content', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('readings', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Review'])

        # Adding M2M table for field topics on 'Review'
        m2m_table_name = db.shorten_name(u'app_review_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('review', models.ForeignKey(orm[u'app.review'], null=False)),
            ('topic', models.ForeignKey(orm[u'app.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['review_id', 'topic_id'])

        # Adding M2M table for field scores on 'Review'
        m2m_table_name = db.shorten_name(u'app_review_scores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('review', models.ForeignKey(orm[u'app.review'], null=False)),
            ('score', models.ForeignKey(orm[u'app.score'], null=False))
        ))
        db.create_unique(m2m_table_name, ['review_id', 'score_id'])


    def backwards(self, orm):
        # Deleting model 'Critic'
        db.delete_table(u'app_critic')

        # Removing M2M table for field readers on 'Critic'
        db.delete_table(db.shorten_name(u'app_critic_readers'))

        # Removing M2M table for field to_read on 'Critic'
        db.delete_table(db.shorten_name(u'app_critic_to_read'))

        # Deleting model 'Category'
        db.delete_table(u'app_category')

        # Deleting model 'Topic'
        db.delete_table(u'app_topic')

        # Deleting model 'Score'
        db.delete_table(u'app_score')

        # Deleting model 'Review'
        db.delete_table(u'app_review')

        # Removing M2M table for field topics on 'Review'
        db.delete_table(db.shorten_name(u'app_review_topics'))

        # Removing M2M table for field scores on 'Review'
        db.delete_table(db.shorten_name(u'app_review_scores'))


    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'app.critic': {
            'Meta': {'object_name': 'Critic'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'readers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'readers_rel_+'", 'blank': 'True', 'to': u"orm['app.Critic']"}),
            'to_read': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'to_read_rel_+'", 'blank': 'True', 'to': u"orm['app.Critic']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'app.review': {
            'Meta': {'object_name': 'Review'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'critic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Critic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pre_content': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'readings': ('django.db.models.fields.IntegerField', [], {}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Score']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Topic']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'app.score': {
            'Meta': {'object_name': 'Score'},
            'avg': ('django.db.models.fields.IntegerField', [], {}),
            'critic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Critic']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'app.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['app']