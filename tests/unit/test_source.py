import unittest

import os

from modules.entities.apk import Apk
from modules.entities.source import Source

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class SourceTest(unittest.TestCase):

    def test_initializes_from_file(self):
        source = Source(input_file=os.path.join(THIS_DIR, 'resources/sample.csv'))
        expected_apks = [Apk(**{'sha256': '0000003B455A6C7AF837EF90F2EAFFD856E3B5CF49F5E27191430328DE2FA670',
                                'sha1': '9C14D537A7ADB4CFC43D291352F73E05E0CCDD4A',
                                'md5': '3EDFC78AB53521942798AD551027D04F', 'dex_date': '2016-04-05 17:58:46',
                                'apk_size': '10386469', 'pkg_name': 'com.zte.bamachaye', 'vercode': '121',
                                'vt_detection': '0', 'vt_scan_date': '2016-06-15 15:26:44', 'dex_size': '4765888',
                                'markets': 'anzhi'}),
                         Apk(**{'sha256': '00000439A3FFA123C3F9BC45E5E821351B1A5C276871B36447AB80C74261F354',
                                'sha1': '375D6FFD167BB5E7E2935B1B927F87D8E44A9AB4',
                                'md5': '9283C74DD8356C18BB6D94B88B8FDD9B', 'dex_date': '2011-10-25 02:30:56',
                                'apk_size': '1044597', 'pkg_name': 'bmthx.god102409paperi', 'vercode': '6',
                                'vt_detection': '1', 'vt_scan_date': '2014-04-27 06:30:31', 'dex_size': '105660',
                                'markets': 'appchina'})]
        actual_apks = []
        for apk in source:
            actual_apks.append(apk)
        self.assertEqual(actual_apks, expected_apks)

    def test_hadles_commas_in_column(self):
        source = Source(input_file=os.path.join(THIS_DIR, 'resources/commas_in_column.csv'))
        try:
            actual_apk = next(source)
            expected_apk = Apk(**{'sha256': 'BC564D52C6E79E1676C19D9602B1359A33B8714A1DC5FCB8ED602209D0B70266',
                                  'sha1': '1E56DD37F5E9DD8DCA2D41720110DAFDEFF89E90',
                                  'md5': '25839816B7BBB4BB766EC1816C51C3C3', 'dex_date': '2013-11-23 19:41:08',
                                  'apk_size': '8344281', 'pkg_name': 'com.androidemu.gbalvbaoshi,snaggamea',
                                  'vercode': '23', 'vt_detection': '31', 'vt_scan_date': '2018-07-23 15:18:33',
                                  'dex_size': '358188', 'markets': 'VirusShare'})
        finally:
            source.input_file.close()
        self.assertEqual(actual_apk, expected_apk)



if __name__ == '__main':
    unittest.main()
