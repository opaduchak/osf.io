# Generated by Django 4.2.13 on 2025-01-16 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import osf.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0024_institution_link_to_external_reports_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='is_curator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='institution',
            name='institutional_request_access_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noderequest',
            name='is_institutional_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='noderequest',
            name='requested_permissions',
            field=models.CharField(blank=True, choices=[('read', 'read'), ('write', 'write'), ('admin', 'admin')], help_text='The permissions being requested for the node (e.g., read, write, admin).', max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='preprintrequest',
            name='is_institutional_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='noderequest',
            name='request_type',
            field=models.CharField(choices=[('access', 'Access'), ('withdrawal', 'Withdrawal'), ('institutional_request', 'Institutional_Request')], help_text='The specific type of node request (e.g., access request).', max_length=31),
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('_id', models.CharField(db_index=True, default=osf.models.base.generate_object_id, max_length=24, unique=True)),
                ('message_text', models.TextField(help_text='The content of the message. The custom text of a formatted email.')),
                ('message_type', models.CharField(choices=[('institutional_request', 'INSTITUTIONAL_REQUEST')], help_text='The type of message being sent, as defined in MessageTypes.', max_length=50)),
                ('is_sender_BCCed', models.BooleanField(default=False, help_text='The boolean value that indicates whether other institutional admins were BCCed')),
                ('reply_to', models.BooleanField(default=False, help_text="Whether to set the sender's username as the `Reply-To` header in the email.")),
                ('institution', models.ForeignKey(help_text='The institution associated with this message.', on_delete=django.db.models.deletion.CASCADE, to='osf.institution')),
                ('recipient', models.ForeignKey(help_text='The recipient of this message.', on_delete=django.db.models.deletion.CASCADE, related_name='received_user_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(help_text='The user who sent this message.', on_delete=django.db.models.deletion.CASCADE, related_name='sent_user_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, osf.models.base.QuerySetExplainMixin),
        ),
    ]
