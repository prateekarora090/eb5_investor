from crewai import Agent
from tools.pdf_reader import read_pdf

class DocumentProcessor(Agent):
    def __init__(self, llm):
        super().__init__(
            role="Document Processor",
            goal="Extract and summarize information from PDFs and other documents",
            backstory="Expert in parsing and summarizing complex documents with years of experience in data extraction.",
            allow_delegation=False,
            llm=llm,
            tools=[read_pdf]
        )
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        with open('knowledge_bases/document_processing.txt', 'r') as file:
            return file.read()
