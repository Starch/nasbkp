# coding=utf-8

# Copyright (C) 2014, Alexandre Vaissière
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
# OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.\

"""Commands for manipulating a zfs filesystem."""

from __future__ import unicode_literals

import subprocess


class Cmd(object):
    """Tiny wrapper around a command, to have logging for free."""

    def __init__(self, cmd, **kwargs):
        self.cmd = cmd

    def __str__(self):
        return ' '.join(self.cmd)


class Zfs(object):
    def __init__(self, volume):
        self.volume = volume

    def snapshots(self):
        """Yields all snapshots on this volume"""
        pass

    def create_snapshot(self, name):
        """Creates a new snapshot on this volume."""
        subprocess.check_output(['zfs', 'snapshot', self.volume + '@' + name], shell=False)
        # TODO check result

