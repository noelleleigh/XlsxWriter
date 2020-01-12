###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2020, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('chart_axis45.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()
        chart = workbook.add_chart({'type': 'bar'})

        chart.axis_ids = [108178048, 108321408]

        data = [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],

        ]

        worksheet.write_column('A1', data[0])
        worksheet.write_column('B1', data[1])
        worksheet.write_column('C1', data[2])

        chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
        chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
        chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

        chart.set_x_axis({
            'name': 'XXX',
            'name_font': {'rotation': 270, 'baseline': -1},
            'num_font': {'rotation': 270, 'baseline': -1}
        })

        chart.set_y_axis({
            'name': 'YYY',
            'name_font': {'rotation': 270, 'baseline': -1},
            'num_font': {'rotation': 270, 'baseline': -1}
        })

        worksheet.insert_chart('E9', chart)

        workbook.close()

        self.assertExcelEqual()