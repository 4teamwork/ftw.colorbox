from ftw.upgrade import UpgradeStep


class AddBrowserLayer(UpgradeStep):
    """Add browser layer.
    """

    def __call__(self):
        self.install_upgrade_profile()
