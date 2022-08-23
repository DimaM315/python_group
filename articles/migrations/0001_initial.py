# Generated by Django 3.1.6 on 2021-02-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(blank=True, upload_to='articles_preview', verbose_name='Картинка')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Загаловок')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['id'],
            },
        ),
    ]