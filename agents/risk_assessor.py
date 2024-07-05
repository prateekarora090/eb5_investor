from crewai import Agent
from .base_agent import BaseAgent

class RiskAssessor(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="Risk Assessor",
            goal="Evaluate potential risks in each EB-5 investment",
            backstory="Expert in risk identification and mitigation strategies for investment projects, with a focus on EB-5 investments.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/risk_assessment.txt', 'r') as file:
            return file.read()