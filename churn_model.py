import numpy as np
import random
from datetime import datetime, timedelta
import pandas as pd

def predict_churn_risk_simplified_rnn(event_sequence, customer_history_length=30):
    """
    Simulates a simplified Recurrent Neural Network (RNN)-like model for churn prediction.
    It analyzes recent customer activity patterns to infer churn risk.
    Higher risk is associated with more 'inactivity' or 'support_query' events recently.

    Args:
        event_sequence (list): A list of event dictionaries for a customer.
        customer_history_length (int): The number of most recent events to consider for prediction.

    Returns:
        float: A churn probability between 0 and 1.
    """
    recent_events = event_sequence[-customer_history_length:] # Focus on recent history

    # Weighted sum of negative (churn-inducing) and positive (retention-inducing) events
    score = 0
    # Assign higher weights to more recent events, simulating temporal importance
    weights = np.linspace(0.1, 1.0, len(recent_events))

    for i, event in enumerate(recent_events):
        weight = weights[i]
        if event['type'] == 'inactivity':
            score += 0.2 * weight # Inactivity strongly increases risk
        elif event['type'] == 'support_query':
            score += 0.15 * weight # Support queries increase risk, might indicate frustration
        elif event['type'] == 'make_purchase':
            score -= 0.1 * weight # Purchases decrease risk, indicates engagement
        elif event['type'] == 'upgrade_plan':
            score -= 0.2 * weight # Upgrades significantly decrease risk, strong commitment
        elif event['type'] == 'login' or event['type'] == 'view_feature':
            score -= 0.05 * weight # General activity decreases risk

    # Map the score to a churn probability using a sigmoid-like function
    # This transforms the raw score into a value between 0 and 1.
    churn_prob = 1 / (1 + np.exp(-score))
    return min(1.0, max(0.0, churn_prob)) # Ensure probability is strictly between 0 and 1

def monte_carlo_churn_prediction(customer_data, num_simulations=100, forecast_days=90):
    """
    Performs Monte Carlo simulations to predict future churn risk.
    For each simulation, it projects future events and re-evaluates churn probability.

    Args:
        customer_data (dict): A dictionary containing customer information, including 'events' and 'last_activity_date'.
        num_simulations (int): The number of Monte Carlo simulations to run.
        forecast_days (int): The number of days into the future to forecast events.

    Returns:
        tuple: A tuple containing:
            - float: The mean churn probability across all simulations.
            - float: The standard deviation of churn probabilities across all simulations.
            - list: A list of all simulated churn probabilities.
    """
    churn_probabilities = []
    
    # Get the current churn risk based on the customer's historical data
    current_risk = predict_churn_risk_simplified_rnn(customer_data['events'])
    
    # Simulate future activity for the next 'forecast_days' for each simulation run
    for _ in range(num_simulations):
        simulated_events_for_forecast = []
        # Start simulating from the day after the last recorded activity
        sim_current_date = datetime.strptime(customer_data['last_activity_date'], '%Y-%m-%d') + timedelta(days=1)
        
        for day_forecast in range(forecast_days):
            # Simulate daily activity for the future based on current risk
            # Higher current risk implies lower likelihood of future positive activity
            activity_prob = 0.6 * (1 - current_risk) # Adjust base activity by current risk
            if random.random() < activity_prob:
                # Randomly pick a positive event type for future activity
                event_type = random.choice(['login', 'view_feature', 'make_purchase', 'support_query'])
                simulated_events_for_forecast.append({'date': sim_current_date.strftime('%Y-%m-%d'), 'type': event_type})
            else:
                simulated_events_for_forecast.append({'date': sim_current_date.strftime('%Y-%m-%d'), 'type': 'inactivity'})
            
            sim_current_date += timedelta(days=1)

        # Combine historical and simulated future events to create a full sequence
        full_event_sequence = customer_data['events'] + simulated_events_for_forecast
        
        # Re-evaluate churn probability with the simulated future events
        sim_churn_prob = predict_churn_risk_simplified_rnn(full_event_sequence)
        churn_probabilities.append(sim_churn_prob)

    return np.mean(churn_probabilities), np.std(churn_probabilities), churn_probabilities

if __name__ == '__main__':
    # Example usage if this file is run directly
    print("Running churn_model.py directly. Demonstrating prediction and Monte Carlo.")
    # Create a dummy customer for testing
    dummy_customer_data = {
        'customer_id': 'TEST-001',
        'start_date': '2023-01-01',
        'last_activity_date': '2024-06-15',
        'churned': False,
        'churn_date': None,
        'events': [
            {'date': '2024-06-01', 'type': 'login'},
            {'date': '2024-06-05', 'type': 'inactivity'},
            {'date': '2024-06-08', 'type': 'view_feature'},
            {'date': '2024-06-10', 'type': 'inactivity'},
            {'date': '2024-06-12', 'type': 'support_query'},
            {'date': '2024-06-15', 'type': 'login'},
        ],
        'churn_propensity_true': 0.3 # Not used in prediction, but part of data structure
    }

    print(f"\nInitial churn risk for TEST-001: {predict_churn_risk_simplified_rnn(dummy_customer_data['events']):.2f}")
    
    mean_prob, std_prob, all_probs = monte_carlo_churn_prediction(dummy_customer_data, num_simulations=50)
    print(f"Monte Carlo Mean Churn Probability: {mean_prob:.2f}")
    print(f"Monte Carlo Std Dev: {std_prob:.2f}")
    import matplotlib.pyplot as plt
    plt.hist(all_probs, bins=10, edgecolor='black')
    plt.title("Simulated Churn Probabilities for TEST-001")
    plt.show()
