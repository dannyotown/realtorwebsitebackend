# Generated by Django 3.1.2 on 2020-10-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('price', models.IntegerField()),
                ('amount_of_beds', models.IntegerField()),
                ('amount_of_baths', models.IntegerField()),
                ('square_feet', models.IntegerField()),
            ],
        ),
    ]