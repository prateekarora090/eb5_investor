import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.financial_analyst import FinancialAnalyst

class TestFinancialAnalyst(unittest.TestCase):
    @patch('crewai.agent.ChatOpenAI')
    def setUp(self, mock_chat_openai):
        mock_chat_openai.return_value = MagicMock()
        self.analyst = FinancialAnalyst(llm=mock_chat_openai.return_value, knowledge_base_path="knowledge_bases/financial_analysis.txt")

    @patch('crewai.agent.ChatOpenAI')
    @patch('agents.financial_analyst.open', new_callable=unittest.mock.mock_open, read_data="Sample knowledge base content")
    def test_load_knowledge_base(self, mock_file, mock_chat_openai):
        analyst = FinancialAnalyst(llm=mock_chat_openai.return_value, knowledge_base_path="knowledge_bases/financial_analysis.txt")
        kb = analyst.load_knowledge_base()
        self.assertEqual(analyst.knowledge_base, "Sample knowledge base content")

    @patch('agents.base_agent.BaseAgent.semantic_search')
    def test_analyze(self, mock_semantic_search):
        mock_semantic_search.return_value = [("score", "relevant info", "source")]
        mock_context = MagicMock()
        result = self.analyst.analyze(mock_context)
        self.assertIn('capital structure', result)
        self.assertIn('financial projections', result)
        self.assertIn('potential_blind_spots', result)
        mock_semantic_search.assert_called()

    def test_identify_blind_spots(self):
        analysis_result = {
            'area1': {'summary': 'cash flow projections'},
            'area2': {'summary': 'risk factors'}
        }
        blind_spots = self.analyst.identify_blind_spots(analysis_result)
        self.assertIn('Missing information on exit strategy', blind_spots)
        self.assertIn('Missing information on job creation estimates', blind_spots)

    def test_analyze_area(self):
        area = "test area"
        relevant_info = [("score", "info1", "source1"), ("score", "info2", "source2")]
        result = self.analyst.analyze_area(area, relevant_info)
        print("result: " + str(result))
        print("result['summary']: " + result['summary'])
        expected_summary = f"Analysis of {area} based on 2 relevant pieces of information:\n- info1... (Source: source1)\n- info2... (Source: source2)\n"
        self.assertTrue(result['summary'].startswith(f"Analysis of {area} based on 2 relevant pieces of information"))

    @patch('agents.base_agent.BaseAgent.set_context')
    def test_set_context(self, mock_set_context):
        mock_context = MagicMock()
        self.analyst.set_context(mock_context)
        mock_set_context.assert_called_once_with(mock_context)

if __name__ == '__main__':
    unittest.main()