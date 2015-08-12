from ftw.upgrade import UpgradeStep


class AddImageScale(UpgradeStep):
    """Add image scale.
    """

    def __call__(self):
        self.install_upgrade_profile()
