import unittest

import HtmlTestRunner

from saptamana6_wk.teste.login_page_test import LoginPageTest
from saptamana6_wk.teste.product_page_test import ProductsPageTest

# instalam libraria html-testRunner
# pip install html-testRunner
class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        # tests_to_run.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(LoginPageTest))
        # tests_to_run.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ProductsPageTest))
        tests_to_run.addTests(
            [unittest.defaultTestLoader.loadTestsFromTestCase(LoginPageTest),
             unittest.defaultTestLoader.loadTestsFromTestCase(ProductsPageTest)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Sauce Labs Test Report",
            report_name="report"
        )

        runner.run(tests_to_run)