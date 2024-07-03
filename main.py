from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini model
gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Import agents (we'll create these next)
from agents.document_processor import DocumentProcessor
from agents.financial_analyst import FinancialAnalyst
# ... import other agents

# Import tools (we'll create these next)
from tools.pdf_reader import read_pdf
from tools.web_scraper import scrape_website
# ... import other tools

# Main workflow
def analyze_investments(investments):
    agents = [
        DocumentProcessor(llm=gemini_llm),
        FinancialAnalyst(llm=gemini_llm),
        # ... other agents
    ]

    tasks = []
    for investment in investments:
        tasks.extend([
            Task(
                description=f"Process documents for investment {investment['id']}",
                agent=agents[0]  # Document Processor
            ),
            Task(
                description=f"Analyze financials for investment {investment['id']}",
                agent=agents[1]  # Financial Analyst
            ),
            # ... other tasks
        ])

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=2
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
    investments = [
        {"id": "1", "folder_id": "folder1", "website": "http://example1.com"},
        {"id": "2", "folder_id": "folder2", "website": "http://example2.com"},
    ]
    result = analyze_investments(investments)
    print(result)