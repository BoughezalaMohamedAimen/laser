# Generated by Django 2.1.9 on 2019-10-09 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonnement',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='abonnement',
            name='nbr_mois',
        ),
        migrations.RemoveField(
            model_name='client',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='client',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='client',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='client',
            name='date_fin',
        ),
        migrations.RemoveField(
            model_name='client',
            name='date_naissance',
        ),
        migrations.RemoveField(
            model_name='client',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='client',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='client',
            name='status',
        ),
        migrations.RemoveField(
            model_name='client',
            name='telephone_urgence',
        ),
    ]