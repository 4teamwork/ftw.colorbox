from ftw.upgrade import UpgradeStep


class AddExcludeSettings(UpgradeStep):
    """Add exclude settings.
    """

    def __call__(self):
        self.install_upgrade_profile()
