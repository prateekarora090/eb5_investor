import unittest
import sys
import os
import json

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from context_assembler.context_assembler import ContextAssembler

class TestSearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.assembler = ContextAssembler('preprocessing/outputs/preprocessed_data')
        self.context = self.assembler.assemble_context("1")  # investment id = "1"

    def test_semantic_search_relevance(self):
        query = "job creation requirements"
        results = self.assembler.semantic_search(self.context, query)
        self.assertTrue(any("job" in result[1].lower() for result in results))
        self.assertTrue(any("creation" in result[1].lower() for result in results))

    def test_search_accuracy(self):
        known_fact = "The investment requires $900,000 in a TEA"
        results = self.assembler.semantic_search(self.context, known_fact)
        self.assertTrue(any("900,000" in result[1] for result in results))
        self.assertTrue(any("TEA" in result[1] for result in results))

if __name__ == '__main__':
    unittest.main()