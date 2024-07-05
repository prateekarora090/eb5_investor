from crewai import Agent
from .base_agent import BaseAgent

class FinancialAnalyst(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="Financial Analyst",
            goal="Analyze financial aspects of EB-5 investments",
            backstory="Experienced financial analyst specializing in EB-5 investments with a strong background in financial modeling and ROI calculations.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/financial_analysis.txt', 'r') as file:
            return file.read()