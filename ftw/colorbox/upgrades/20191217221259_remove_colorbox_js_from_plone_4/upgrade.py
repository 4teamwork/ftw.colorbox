from ftw.upgrade import UpgradeStep
from Products.CMFPlone.utils import getFSVersionTuple


IS_PLONE_4 = getFSVersionTuple() < (5, )


class RemoveColorboxJsFromPlone4(UpgradeStep):
    """Remove redundant colorbox.js from Plone 4.
    """

    def __call__(self):
        if IS_PLONE_4:
            self.install_upgrade_profile()
