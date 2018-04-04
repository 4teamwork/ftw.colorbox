from ftw.upgrade import UpgradeStep


class AddColorboxJs(UpgradeStep):
    """Add colorbox js.
    """

    def __call__(self):
        self.install_upgrade_profile()
