#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pavan.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
class Migration(migrations.Migration):

    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

from django.contrib import admin

from .models import Article

admin.site.register(Article)

from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'

from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'title',
            'content',
            'active',
        ]