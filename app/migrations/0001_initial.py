# Generated by Django 3.2.9 on 2021-11-27 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=40)),
                ('cover', models.ImageField(upload_to='book_covers')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
