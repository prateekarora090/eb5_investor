from crewai import Agent
from .base_agent import BaseAgent

class InvestmentComparator(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="Investment Comparator",
            goal="Compare and rank EB-5 investments based on various criteria",
            backstory="Experienced investment analyst skilled in multi-criteria decision analysis and comparative investment evaluation.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/investment_comparison.txt', 'r') as file:
            return file.read()