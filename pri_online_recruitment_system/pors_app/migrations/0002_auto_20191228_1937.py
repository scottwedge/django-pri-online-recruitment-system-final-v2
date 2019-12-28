# Generated by Django 2.2.3 on 2019-12-28 11:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='erp_question',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Referral', 'Referral'), ('Online Job Portal', 'Online Job Portal'), ('Leaflets', 'Leaflets'), ('Walk-in', 'Walk-in'), ('Job fair', 'Job fair')], max_length=52, verbose_name='How did you found out about thid job?'),
        ),
    ]