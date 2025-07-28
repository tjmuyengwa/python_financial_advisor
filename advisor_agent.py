# advisor_agent.py
import os

from dotenv import load_dotenv
from google import genai
from advisor_prompt import advisor_template

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


def run_financial_advisor(user_data: dict) -> str:
    """
    Sends the formatted user profile to Gemini and returns the AI's response.
    """
    prompt = advisor_template.format(
        income=user_data["income"],
        expenses=user_data["monthly_expenses"],
        goals=", ".join(user_data["financial_goals"]),
        risk=user_data["risk_tolerance"],
    )

    client = genai.Client(
        api_key=api_key,
    )  # reads GEMINI_API_KEY from env
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
