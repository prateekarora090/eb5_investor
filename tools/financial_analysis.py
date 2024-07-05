# tools/financial_analysis.py

import numpy as np

def calculate_roi(investment_amount, projected_returns, time_period):
    roi = (projected_returns - investment_amount) / investment_amount
    annualized_roi = (1 + roi) ** (1 / time_period) - 1
    return roi, annualized_roi

def assess_risk(volatility, market_correlation):
    risk_score = volatility * 0.7 + market_correlation * 0.3
    if risk_score < 0.3:
        return "Low"
    elif risk_score < 0.7:
        return "Medium"
    else:
        return "High"

def analyze_financials(investment_data):
    roi, annualized_roi = calculate_roi(
        investment_data['amount'],
        investment_data['projected_returns'],
        investment_data['time_period']
    )
    risk_level = assess_risk(
        investment_data['volatility'],
        investment_data['market_correlation']
    )
    return {
        "ROI": roi,
        "Annualized ROI": annualized_roi,
        "Risk Level": risk_level
    }