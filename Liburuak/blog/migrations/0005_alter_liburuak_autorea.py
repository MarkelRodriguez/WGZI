# Generated by Django 4.2.5 on 2023-09-27 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_autoreak_jaiotze_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liburuak',
            name='autorea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autoreak'),
        ),
    ]
