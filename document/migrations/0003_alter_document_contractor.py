# Generated by Django 4.2 on 2024-11-27 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0001_initial'),
        ('document', '0002_alter_document_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='contractor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='document_contractor', to='contractor.contractor'),
            preserve_default=False,
        ),
    ]