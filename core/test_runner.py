from importlib import import_module

from django.conf import settings
from django.db import connections
from django.test.runner import DiscoverRunner


class CoreTestRunner(DiscoverRunner):
    def setup_test_environment(self, **kwargs):
        """TESTING setting to True. Default is False."""
        super().setup_test_environment(**kwargs)
        settings.TESTING = True

    def setup_databases(self, **kwargs):
        """Set database"""
        kwargs["aliases"] = connections
        r = super().setup_databases(**kwargs)
        self.load_fixtures()
        return r

    @classmethod
    def load_fixtures(cls):
        try:
            module = import_module(f"api.fixtures")
            getattr(module, "run_fixtures")()
        except ImportError:
            return
