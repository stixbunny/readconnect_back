# Generated by Django 4.2.6 on 2023-10-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_toreadlist_readlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='website.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='website.category'),
        ),
        migrations.AlterField(
            model_name='readlist',
            name='booklist',
            field=models.ManyToManyField(related_name='inreadlist', to='website.book'),
        ),
        migrations.AlterField(
            model_name='toreadlist',
            name='booklist',
            field=models.ManyToManyField(related_name='intoreadlist', to='website.book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reviews',
            field=models.ManyToManyField(related_name='reviews', through='website.Review', to='website.book'),
        ),
    ]
