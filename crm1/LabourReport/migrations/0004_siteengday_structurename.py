# Generated by Django 4.1 on 2022-10-28 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LabourReport', '0003_remove_siteengday_structurename'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteengday',
            name='StructureName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.structure'),
        ),
    ]