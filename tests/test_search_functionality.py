import unittest
from context_assembler import ContextAssembler

class TestSearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.assembler = ContextAssembler('preprocessing/outputs/preprocessed_data')
        self.context = self.assembler.assemble_context("1") # investment id = "1"

    def test_semantic_search_relevance(self):
        query = "job creation requirements"
        results = self.context.semantic_search(query)
        self.assertTrue(any("job" in result[1].lower() for result in results))
        self.assertTrue(any("creation" in result[1].lower() for result in results))

    def test_deep_dive_comprehensiveness(self):
        topic = "market analysis"
        deep_dive_result = self.context.deep_dive(topic)
        self.assertGreater(len(deep_dive_result.split()), 200)  # Ensure substantial content
        self.assertTrue("market" in deep_dive_result.lower())
        self.assertTrue("analysis" in deep_dive_result.lower())

    def test_search_accuracy(self):
        known_fact = "The investment requires $900,000 in a TEA"
        results = self.context.semantic_search(known_fact)
        self.assertTrue(any("900,000" in result[1] for result in results))
        self.assertTrue(any("TEA" in result[1] for result in results))

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()