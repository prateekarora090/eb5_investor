from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
import os
import logging
import json
from dotenv import load_dotenv
import argparse
from preprocessing.document_preprocessor import DocumentPreprocessor

# Import agents
from agents.document_processor import DocumentProcessor
from agents.financial_analyst import FinancialAnalyst
from agents.immigration_law_expert import ImmigrationLawExpert
from agents.risk_assessor import RiskAssessor
from agents.market_research_specialist import MarketResearchSpecialist
from agents.eb5_program_specialist import EB5ProgramSpecialist
from agents.investment_comparator import InvestmentComparator

# Import tools
from tools.pdf_reader import read_pdf
from tools.web_scraper import scrape_website
from tools.google_drive_reader import list_files_in_folder, read_file_from_drive

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='eb5_analysis.log'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv('secrets/.env')

# Set API keys
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPEN_AI_API_KEY')

def get_llm(model_name="gemini-pro"):
    if model_name == "gemini-pro":
        return ChatGoogleGenerativeAI(model="gemini-pro")
    elif model_name == "gpt-3.5-turbo":
        return OpenAI(model_name="gpt-3.5-turbo")
    # Add more model options as needed

def analyze_investments(investments, llm):
    # Initialize agents
    document_processor = DocumentProcessor(llm=llm)
    financial_analyst = FinancialAnalyst(llm=llm)
    immigration_expert = ImmigrationLawExpert(llm=llm)
    risk_assessor = RiskAssessor(llm=llm)
    market_researcher = MarketResearchSpecialist(llm=llm)
    eb5_specialist = EB5ProgramSpecialist(llm=llm)
    investment_comparator = InvestmentComparator(llm=llm)

    tasks = []
    for investment in investments:
        # Process preprocessed data
        preprocessed_file = f"preprocessed_data/{investment['id']}/metadata.json"
        with open(preprocessed_file, 'r') as f:
            preprocessed_data = json.load(f)
        
        tasks.extend([
            Task(
                description=f"Analyze financial aspects of investment {investment['id']}",
                agent=financial_analyst,
                context=preprocessed_data
            ),
            Task(
                description=f"Evaluate immigration law compliance for investment {investment['id']}",
                agent=immigration_expert,
                context=preprocessed_data
            ),
            Task(
                description=f"Assess risks for investment {investment['id']}",
                agent=risk_assessor,
                context=preprocessed_data
            ),
            Task(
                description=f"Conduct market research for investment {investment['id']}",
                agent=market_researcher,
                context=preprocessed_data
            ),
            Task(
                description=f"Evaluate EB-5 program compliance for investment {investment['id']}",
                agent=eb5_specialist,
                context=preprocessed_data
            )
        ])

    # Add final comparison task
    tasks.append(
        Task(
            description="Compare and rank all analyzed investments",
            agent=investment_comparator
        )
    )

    crew = Crew(
        agents=[document_processor, financial_analyst, immigration_expert, risk_assessor, 
                market_researcher, eb5_specialist, investment_comparator],
        tasks=tasks,
        verbose=2
    )

    result = crew.kickoff()
    return result

def main():
    parser = argparse.ArgumentParser(description="EB-5 Investment Analysis")
    parser.add_argument("action", choices=["preprocess", "analyze"], help="Action to perform")
    args = parser.parse_args()

    if args.action == "preprocess":
        print("Starting preprocessing. Check 'preprocessing.log' for progress.")
        preprocessor = DocumentPreprocessor()
        preprocessor.preprocess_investments('inputs/options.json')
    elif args.action == "analyze":
        # Get llm
        llm = get_llm("gpt-3.5-turbo")  # Use this for testing
        # llm = get_llm("gemini-pro")  # Use this for final runs
        
        # Read investment options from JSON file
        with open('inputs/options.json', 'r') as f:
            all_investments = json.load(f)
        
        # Only consider the first three options for initial testing
        investments_to_analyze = all_investments[:3]
        
        print(f"Analyzing {len(investments_to_analyze)} investment options")

        # Wrap main functionality in try-except
        try:
            result = analyze_investments(investments_to_analyze, llm)
            print(result)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}", exc_info=True)
            print(f"An error occurred. Please check the log file for details.")

if __name__ == "__main__":
    main()