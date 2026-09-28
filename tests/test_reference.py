import unittest

from reference import find_matches


class TestClinicalReference(unittest.TestCase):

    def test_common_cold(self):
        results = find_matches(
            "cough, runny nose, sneezing"
        )

        self.assertTrue(len(results) > 0)
        self.assertEqual(
            results[0]["condition"],
            "Common Cold"
        )

    def test_influenza(self):
        results = find_matches(
            "fever, cough, headache, fatigue"
        )

        conditions = []

        for result in results:
            conditions.append(result["condition"])

        self.assertIn("Influenza", conditions)

    def test_no_match(self):
        results = find_matches(
            "something_unknown"
        )

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()