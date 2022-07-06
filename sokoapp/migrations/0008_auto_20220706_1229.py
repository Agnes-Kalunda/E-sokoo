# Generated by Django 3.2 on 2022-07-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokoapp', '0007_auto_20220706_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='sokoapp.OrderItem'),
        ),
    ]
