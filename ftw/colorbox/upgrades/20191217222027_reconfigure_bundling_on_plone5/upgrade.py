from ftw.upgrade import UpgradeStep
from Products.CMFPlone.utils import getFSVersionTuple


IS_PLONE_5 = getFSVersionTuple() >= (5, )


class ReconfigureBundlingOnPlone5(UpgradeStep):
    """Reconfigure bundling on Plone5 to use Yarn.
    """

    def __call__(self):
        if IS_PLONE_5:
            self.install_upgrade_profile()
