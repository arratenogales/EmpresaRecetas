# Generated by Django 4.2.7 on 2023-11-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaRecetas', '0007_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('visitor', 'Visitor')], default='user', max_length=20),
            preserve_default=False,
        ),
    ]
