import unittest
import pandas as pd

class TestExpectedCSVOutput(unittest.TestCase):

    def test_expected_output_matches(self):
        # Load expected and actual outputs
        expected_df = pd.read_csv('test/expected_output.csv', delimiter=';')
        actual_df = pd.read_csv('src/customer_item_quantities.csv', delimiter=';')

        # Sort both for fair comparison
        expected_df = expected_df.sort_values(by=["Customer", "Item"]).reset_index(drop=True)
        actual_df = actual_df.sort_values(by=["Customer", "Item"]).reset_index(drop=True)

        # Compare DataFrames
        pd.testing.assert_frame_equal(actual_df, expected_df)

if __name__ == '__main__':
    unittest.main()
