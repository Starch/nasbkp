# coding=utf-8

#  Copyright (C) 2014, Alexandre Vaissière
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

from __future__ import unicode_literals

import unittest

import mock

from nasbkp.storage.zfs import Zfs


class ZfsTest(unittest.TestCase):
    def setUp(self):
        self.zfs = Zfs('tank/volume')

    def test_create(self):
        with mock.patch('nasbkp.storage.zfs.subprocess') as subprocess:
            self.zfs.create_snapshot('toto17')
            subprocess.check_output.assert_called_once_with(['zfs', 'snapshot', 'tank/volume@toto17'], shell=False)


if __name__ == '__main__':
    unittest.main()
