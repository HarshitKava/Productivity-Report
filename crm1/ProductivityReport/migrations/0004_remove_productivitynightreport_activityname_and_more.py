# Generated by Django 4.1 on 2022-11-22 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductivityReport', '0003_remove_productivityreport_activitynamebeta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='ActivityName',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='ActivityNameBeta',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='Areaname',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='ContractorName',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='Deployment',
        ),
        migrations.RemoveField(
            model_name='productivitynightreport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='ActivityName',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='Areaname',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='ContractorName',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='Deployment',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='created_at',
        ),
    ]
