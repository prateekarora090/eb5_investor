from crewai import Agent
from .base_agent import BaseAgent

class EB5ProgramSpecialist(BaseAgent):
    def __init__(self, llm):
        super().__init__(
            role="EB-5 Program Specialist",
            goal="Provide deep insights into EB-5 program requirements and nuances",
            backstory="Expert in EB-5 program regulations with years of experience in successful EB-5 project implementations.",
            allow_delegation=False,
            llm=llm
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/eb5_program.txt', 'r') as file:
            return file.read()