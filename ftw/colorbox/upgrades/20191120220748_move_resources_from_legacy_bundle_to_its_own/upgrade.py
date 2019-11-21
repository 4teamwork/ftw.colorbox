from ftw.upgrade import UpgradeStep
from plone import api
import pkg_resources


IS_PLONE_5 = pkg_resources.get_distribution('Products.CMFPlone').version >= '5'


class MoveResourcesFromLegacyBundleToItsOwn(UpgradeStep):
    """Move resources from legacy bundle to its own.
    """

    def __call__(self):
        if IS_PLONE_5:
            to_remove = [u'resource-ftw-colorbox-resources-jquery-colorbox',
                         u'init-colorbox-js',
                         u'resource-ftw-colorbox-resources-colorbox-js',
                         u'resource-ftw-colorbox-resources-colorbox-css']

            record = 'plone.bundles/plone-legacy.resources'
            resources = api.portal.get_registry_record(record)

            for resource in to_remove:
                if resource in resources:
                    resources.remove(resource)

            self.install_upgrade_profile()
        else:
            # Do nothing on plone 4
            pass
