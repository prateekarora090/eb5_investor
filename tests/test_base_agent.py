import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.base_agent import BaseAgent

class TestBaseAgent(unittest.TestCase):
    @patch('crewai.agent.ChatOpenAI')
    def setUp(self, mock_chat_openai):
        # Create mock data for required fields
        self.agent = BaseAgent(
            name="Test Agent",
            role="Test Role",
            goal="Test Goal",
            backstory="Test Backstory"
        )

        # Configure the mock object
        mock_chat_openai.return_value = MagicMock()

    def test_set_and_get_context(self):
        context = MagicMock()
        self.agent.set_context(context)
        self.assertEqual(self.agent.context, context)

    def test_semantic_search(self):
        mock_context = MagicMock()
        mock_context.semantic_search.return_value = [("score", "result", "source")]
        self.agent.set_context(mock_context)
        results = self.agent.semantic_search("query")
        mock_context.semantic_search.assert_called_with(mock_context, "query", 5)
        self.assertEqual(results, [("score", "result", "source")])

    def test_deep_dive(self):
        mock_context = MagicMock()
        mock_context.semantic_search.return_value = [("score1", "result1", "source1"), ("score2", "result2", "source2")]
        self.agent.set_context(mock_context)
        result = self.agent.deep_dive("topic")
        mock_context.semantic_search.assert_called_with(mock_context, "topic", 10)
        self.assertEqual(result, "result1\n\nresult2")

    def test_semantic_search_no_context(self):
        with self.assertRaises(ValueError):
            self.agent.semantic_search("query")

    # @patch('agents.base_agent.requests.get')
    # def test_web_search(self, mock_get):
    #     mock_response = MagicMock()
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = {'results': ['result1', 'result2']}
    #     mock_get.return_value = mock_response

    #     results = self.agent.web_search("query")
    #     self.assertEqual(results, ['result1', 'result2'])

if __name__ == '__main__':
    unittest.main()