# Generated by Django 3.2 on 2021-04-11 00:44

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownfield.models.MarkdownField(rendered_field='content_rendered', use_editor=False),
        ),
    ]
