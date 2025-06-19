# data_simulator.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_customer_events(num_days, churn_propensity, activity_base_rate=0.5):
    """
    Generates a sequence of simulated customer events for a single customer.

    Args:
        num_days (int): The number of days to simulate events for.
        churn_propensity (float): A value between 0 and 1 indicating the customer's likelihood to churn.
        activity_base_rate (float): Base probability of an activity occurring on any given day.

    Returns:
        tuple: A tuple containing:
            - list: A list of dictionaries, where each dictionary represents an event.
            - bool: True if the customer churned during the simulation, False otherwise.
            - int or None: The day index (from start_date) on which the customer churned, or None if no churn.
    """
    events = []
    current_date = datetime.now() - timedelta(days=num_days)
    churned = False
    churn_day = None

    for day in range(num_days):
        # Simulate daily activity: higher churn propensity implies lower activity likelihood
        activity_prob = activity_base_rate * (1 - churn_propensity)
        if random.random() < activity_prob:
            event_type = random.choice(['login', 'view_feature', 'make_purchase', 'support_query', 'upgrade_plan'])
            events.append({'date': current_date.strftime('%Y-%m-%d'), 'type': event_type})
        else:
            events.append({'date': current_date.strftime('%Y-%m-%d'), 'type': 'inactivity'})

        # Simulate churn based on propensity
        daily_churn_prob = churn_propensity / num_days  # Distribute propensity over days
        if not churned and random.random() < daily_churn_prob:
            churned = True
            churn_day = day
            events.append({'date': current_date.strftime('%Y-%m-%d'), 'type': 'churned'})
            break  # Customer churns, no more events

        current_date += timedelta(days=1)

    return events, churned, churn_day

def simulate_customer_data(num_customers=100):
    """
    Generates a synthetic customer dataset with simulated events and churn status.

    Args:
        num_customers (int): The number of customers to simulate.

    Returns:
        pd.DataFrame: A DataFrame containing simulated customer data.
    """
    customers = []
    for i in range(num_customers):
        customer_id = f"CUST-{i:04d}"
        start_date = datetime.now() - timedelta(days=random.randint(30, 365))
        num_days_active = (datetime.now() - start_date).days
        
        # Churn propensity: higher value means higher likelihood of churning
        churn_propensity = np.random.beta(a=1, b=5) # Skewed towards lower churn (most customers won't churn easily)

        events, churned, churn_day_idx = generate_customer_events(num_days_active, churn_propensity)
        
        churn_date = None
        if churned:
            # Find the actual churn event date from the events list
            churn_event = next((e for e in events if e['type'] == 'churned'), None)
            if churn_event:
                churn_date = churn_event['date']
            else: # Fallback in case 'churned' event wasn't explicitly added
                churn_date = (start_date + timedelta(days=churn_day_idx)).strftime('%Y-%m-%d')
        
        customers.append({
            'customer_id': customer_id,
            'start_date': start_date.strftime('%Y-%m-%d'),
            'last_activity_date': events[-1]['date'] if events else start_date.strftime('%Y-%m-%d'),
            'churned': churned,
            'churn_date': churn_date,
            'events': events,
            'churn_propensity_true': churn_propensity # For evaluation/comparison in a real scenario
        })
    return pd.DataFrame(customers)

if __name__ == '__main__':
    # Example usage if this file is run directly
    print("Running data_simulator.py directly. Generating sample data...")
    sample_df = simulate_customer_data(num_customers=5)
    print(sample_df[['customer_id', 'start_date', 'churned', 'churn_date', 'churn_propensity_true']].to_string())
    print("\nFirst customer's events:")
    if not sample_df.empty:
        print(pd.DataFrame(sample_df.iloc[0]['events']).to_string())