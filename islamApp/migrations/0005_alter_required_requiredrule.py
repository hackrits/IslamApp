# Generated by Django 4.1.6 on 2023-02-26 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('islamApp', '0004_alter_required_requirementstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='required',
            name='requiredrule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='islamApp.grouprules'),
        ),
    ]