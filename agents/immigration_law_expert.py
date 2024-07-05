from crewai import Agent
from .base_agent import BaseAgent

class ImmigrationLawExpert(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="Immigration Law Expert",
            goal="Evaluate immigration law compliance of EB-5 investments",
            backstory="Seasoned immigration attorney with extensive experience in EB-5 visa applications and compliance issues.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/immigration_law.txt', 'r') as file:
            return file.read()