# Generated by Django 4.2 on 2024-11-24 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contractor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statment', models.CharField(max_length=120)),
                ('file', models.FileField(upload_to='files')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('notes', models.TextField(max_length=1500)),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_contractor', to='contractor.contractor')),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_documenttype', to='settings.document_type')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
