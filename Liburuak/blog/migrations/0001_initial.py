# Generated by Django 4.2.5 on 2023-09-25 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autoreak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('abizena', models.CharField(max_length=100)),
                ('jaiotze_data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Liburuak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izenburua', models.CharField(max_length=100)),
                ('edukia', models.CharField(max_length=300)),
                ('noizsortua', models.DateTimeField(auto_now_add=True)),
                ('autorea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autoreak')),
            ],
        ),
    ]
