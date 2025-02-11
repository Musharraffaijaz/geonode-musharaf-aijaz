# Generated by Django 3.2.21 on 2023-10-05 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0085_alter_resourcebase_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_to', to='base.resourcebase')),
                ('target', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='linked_by', to='base.resourcebase')),
                ('internal', models.BooleanField(default=False)),
            ],
        ),
    ]
