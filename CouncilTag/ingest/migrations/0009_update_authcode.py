# Generated by Django 2.0.7 on 2018-07-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0008_meeting_id_to_agenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='engageuserprofile',
            name='authcode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='authcode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]