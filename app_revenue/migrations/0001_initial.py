# Generated by Django 4.2.5 on 2023-10-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue_types', models.CharField(choices=[('SAL', 'Salary'), ('BEN', 'Benefits'), ('OUT', 'Others')], default='OUT', max_length=3, verbose_name='Revenue Type')),
                ('month', models.PositiveIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='Month')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('value_revenue', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Value Revenue')),
            ],
            options={
                'verbose_name': 'Revenue',
                'verbose_name_plural': 'Revenues',
                'ordering': ['year', 'month'],
            },
        ),
    ]
