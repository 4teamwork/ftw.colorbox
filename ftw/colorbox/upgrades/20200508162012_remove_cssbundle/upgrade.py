from ftw.upgrade import UpgradeStep
import pkg_resources


class RemoveCssbundle(UpgradeStep):
    """Remove cssbundle.
    """

    def __call__(self):
        IS_PLONE_5 = pkg_resources.get_distribution('Products.CMFPlone').version >= '5'
        if IS_PLONE_5:
            self.install_upgrade_profile()
