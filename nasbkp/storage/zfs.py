
"""Commands for manipulating a zfs filesystem."""


class Zfs(object):
    def __init__(self, volume):
        self.volume = volume

    def snapshots(self):
        """Yields all snapshots on this volume"""
        pass

    def create_snapshot(self, name):
        """Creates a new snapshot on this volume."""
        pass

