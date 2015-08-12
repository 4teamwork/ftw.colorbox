from Products.CMFCore.utils import getToolByName
from ftw.colorbox.tests import FunctionalTestCase


class TestInstallation(FunctionalTestCase):

    def test_generic_setup_profile_is_installed(self):
        portal_setup = getToolByName(self.layer['portal'], 'portal_setup')
        version = portal_setup.getLastVersionForProfile('ftw.colorbox:default')
        self.assertNotEquals('unknown', version)
