def suggest_intervention(churn_probability):
    """
    Suggests interventions based on a calculated churn probability.

    Args:
        churn_probability (float): The predicted churn probability for a customer (between 0 and 1).

    Returns:
        dict: A dictionary containing intervention details, including title, description,
              recommended actions, and a suggested color for display.
    """
    if churn_probability >= 0.7:
        return {
            "title": "High Churn Risk: Urgent Intervention Needed!",
            "description": "This customer is highly likely to churn soon. Immediate and personalized action is critical.",
            "actions": [
                "Personalized email/call from Account Manager to understand concerns.",
                "Offer a significant discount or tailored loyalty program.",
                "Conduct a 'win-back' survey if churn is imminent."
            ],
            "color": "red" # Color for display purposes
        }
    elif churn_probability >= 0.4:
        return {
            "title": "Moderate Churn Risk: Proactive Engagement Advised.",
            "description": "There's a noticeable risk of churn. Proactive measures can help retain this customer.",
            "actions": [
                "Send targeted content or feature usage tips.",
                "Offer a small, personalized incentive.",
                "Gather feedback through a short survey on recent experience."
            ],
            "color": "orange"
        }
    else:
        return {
            "title": "Low Churn Risk: Monitor & Nurture.",
            "description": "Customer seems stable, but continuous nurturing is always beneficial.",
            "actions": [
                "Continue regular communication and product updates.",
                "Encourage participation in community or beta programs.",
                "Maintain high-quality support and service."
            ],
            "color": "green"
        }

if __name__ == '__main__':
    # Example usage if this file is run directly
    print("Running intervention_strategy.py directly. Demonstrating suggestions:")
    print("\n--- High Risk (0.8) ---")
    high_risk_suggestion = suggest_intervention(0.8)
    print(f"Title: {high_risk_suggestion['title']}")
    print("Actions:")
    for action in high_risk_suggestion['actions']:
        print(f"- {action}")

    print("\n--- Moderate Risk (0.5) ---")
    moderate_risk_suggestion = suggest_intervention(0.5)
    print(f"Title: {moderate_risk_suggestion['title']}")
    print("Actions:")
    for action in moderate_risk_suggestion['actions']:
        print(f"- {action}")

    print("\n--- Low Risk (0.2) ---")
    low_risk_suggestion = suggest_intervention(0.2)
    print(f"Title: {low_risk_suggestion['title']}")
    print("Actions:")
    for action in low_risk_suggestion['actions']:
        print(f"- {action}")
