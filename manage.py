#!/usr/bin/env python
import os
import sys
from acm_soda import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acm_soda.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


#!/usr/bin/python
#from django.core.management import execute_manager
#from acm_soda import settings

#try:
#    pass
#except ImportError:
#    import sys
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#    sys.exit(1)

#if __name__ == "__main__":
#    execute_manager(settings)
