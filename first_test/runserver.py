#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_test.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    args = sys.argv
    args += [
         '8000', '--noreload', '--insecure'
    ]
    execute_from_command_line(args)




'''
        execute_from_command_line(sys.argv)


#!/usr/bin/env python3

#import addimportpaths
import os
import sys
#from debtools import patchit

if __name__ == "main":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cryptotrading.settings")

    from django.core.management import execute_from_command_line
    args = sys.argv
    args += [
        'runserver','8080','--noreload','--insecure'
    ]
    execute_from_command_line(args)
'''