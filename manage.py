#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# django-admin startproject 名字(创建一个django项目)
# python manage.py runserver 127.0.0.1:8080(此处不加参数默认监听8000)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
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
