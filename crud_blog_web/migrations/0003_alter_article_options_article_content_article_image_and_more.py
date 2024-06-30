# Generated by Django 5.0.4 on 2024-04-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_blog_web', '0002_article_year_alter_article_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Artykuły'},
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
