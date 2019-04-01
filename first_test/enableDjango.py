import os
import sys


class g: pass
G=g()

def enable_django():
    from django.apps import apps
    dj_path = os.path.dirname(os.path.dirname(__file__))
    G.DJANGO_PROJECT_PATH = dj_path
    G.DJANGO_SETTINGS_MODULE = "first_test.settings"
    if not apps.apps_ready:
        print('loading django')
        path = sys.path
        if dj_path not in path:
            path.append(dj_path)

        set_django_settings_module()
        import django
        django.setup()

def set_django_settings_module():
    # from . import globs as G
    # path = G.AMSWEBSERVER_PATH
    # if path not in sys.path:
        # sys.path.insert(0, path)

    env = os.environ
    if True:
        env["DJANGO_SETTINGS_MODULE"] = G.DJANGO_SETTINGS_MODULE
    else:
        env.setdefault(
            "DJANGO_SETTINGS_MODULE",
            G.DJANGO_SETTINGS_MODULE
        )



enable_django()


print
