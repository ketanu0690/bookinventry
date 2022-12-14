# Generated by Django 4.1 on 2022-08-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_image',
            field=models.ImageField(default='avatar.jpg', upload_to='Book_Images'),
        ),
        migrations.AddField(
            model_name='store',
            name='store_image',
            field=models.ImageField(default='default.jpg', upload_to='Store_Images'),
        ),
    ]
