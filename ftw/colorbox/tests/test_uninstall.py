from ftw.testing.genericsetup import GenericSetupUninstallMixin
from ftw.testing.genericsetup import apply_generic_setup_layer
from unittest import TestCase


@apply_generic_setup_layer
class TestGenericSetupUninstall(TestCase, GenericSetupUninstallMixin):
    package = 'ftw.colorbox'
    # FIXME - we shouldn't need to have to do this
    skip_files = ('registry.xml',)
