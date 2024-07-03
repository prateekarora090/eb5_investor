from crewai import Agent

class DocumentProcessor(Agent):
    def __init__(self, llm):
        super().__init__(
            role="Document Processor",
            goal="Extract and summarize information from PDFs and other documents",
            backstory="Expert in parsing and summarizing complex documents with years of experience in data extraction.",
            allow_delegation=False,
            llm=llm
        )