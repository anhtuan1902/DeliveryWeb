# Generated by Django 4.2 on 2023-05-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('CANCEL', 'CANCEL'), ('CONFIRM', 'CONFIRM'), ('DELIVERING', 'DELIVERING'), ('RECEIVED', 'RECEIVED')], default='RECEIVED', max_length=12),
        ),
    ]
