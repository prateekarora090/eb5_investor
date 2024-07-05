from crewai import Agent
from .base_agent import BaseAgent

class MarketResearchSpecialist(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="Market Research Specialist",
            goal="Analyze market trends and identify potential alternative investments",
            backstory="Experienced market researcher with a keen eye for emerging trends and opportunities in the EB-5 investment landscape.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/market_research.txt', 'r') as file:
            return file.read()