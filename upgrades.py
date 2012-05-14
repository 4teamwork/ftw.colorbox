from plone.app.upgrade.utils import loadMigrationProfile


def upgrade_to_v1001(context):    
    loadMigrationProfile(context, 'profile-ftw.colorbox:to_v1001')
