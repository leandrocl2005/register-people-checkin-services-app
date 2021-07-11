# Generated by Django 3.1.5 on 2021-05-17 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('checkin', '0002_auto_20210517_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='companioncheckin',
            name='patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='patient', to='people.person', verbose_name='Paciente'),
            preserve_default=False,
        ),
    ]