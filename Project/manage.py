#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_podcast_backend.settings')
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


from django.core.management.commands.runserver import Command as runserver

original_runserver= runserver.handle

def new_runserver(self, *args, **options):
    original_runserver(self, *args, **options)
    print("\n Available Routes:")
    print(" Signup Page: http://127.0.0.1:8000/auth/signup/")
    print("Login Page: http://127.0.0.1:8000/auth/login/")
    print("Admin Panel: http://127.0.0.1:8000/admin/")

runserver.handle = new_runserver