# Generated by Django 5.1.1 on 2024-10-18 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyProducts', '0003_alter_product_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Chicken', 'Chicken'), ('Egg', 'Egg')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='Chicken', on_delete=django.db.models.deletion.CASCADE, to='EasyProducts.category'),
            preserve_default=False,
        ),
    ]