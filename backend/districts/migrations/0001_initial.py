# Generated by Django 4.1 on 2022-09-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postman', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictStreet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postman.postman', verbose_name='Почтальон')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Улица участка',
                'verbose_name_plural': 'Улицы участка',
                'db_table': 'district_street',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер участка')),
                ('title', models.CharField(max_length=100, verbose_name='Название участка')),
                ('district_street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='districts.districtstreet', verbose_name='Улицы участка')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
                'db_table': 'district',
            },
        ),
    ]