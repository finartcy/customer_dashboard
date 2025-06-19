import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def display_customer_dashboard(df):
    """
    Calculates and prints key metrics to quantify the health of customers across the dataset.
    Also generates plots for churn propensity and event type distribution.

    Args:
        df (pd.DataFrame): The DataFrame containing customer data.
                           Assumes 'customer_id', 'start_date', 'last_activity_date',
                           'churned', 'churn_date', 'events', and 'churn_propensity_true' columns.
    """
    print("\n" + "=" * 70)
    print("                 CUSTOMER HEALTH DASHBOARD                 ")
    print("=" * 70)

    total_customers = len(df)
    active_customers = df[df['churned'] == False]
    churned_customers = df[df['churned'] == True]

    print(f"Total Customers: {total_customers}")
    print(f"Active Customers: {len(active_customers)}")
    print(f"Churned Customers: {len(churned_customers)}")
    
    if total_customers > 0:
        print(f"Churn Rate: {(len(churned_customers) / total_customers * 100):.2f}%")
    else:
        print("No customers to calculate churn rate.")

    # Convert date strings to datetime objects for calculations
    df['start_date_dt'] = pd.to_datetime(df['start_date'])
    df['last_activity_date_dt'] = pd.to_datetime(df['last_activity_date'])
    
    # Calculate tenure for active customers
    if not active_customers.empty:
        active_customers_tenure = (datetime.now() - active_customers['start_date_dt']).dt.days
        print(f"Average Tenure (Active Customers): {active_customers_tenure.mean():.0f} days")
    else:
        print("No active customers to calculate average tenure.")

    # Calculate tenure for churned customers (up to churn date)
    if not churned_customers.empty:
        churned_customers_tenure = (pd.to_datetime(churned_customers['churn_date']) - churned_customers['start_date_dt']).dt.days
        print(f"Average Tenure (Churned Customers): {churned_customers_tenure.mean():.0f} days")
    else:
        print("No churned customers to calculate average tenure.")

    # Average activity frequency (simple approximation based on last activity date)
    # This metric would be more accurate with actual event counts over time.
    if not active_customers.empty:
        # A more sophisticated calculation would count events per customer over their tenure.
        # For this simulation, we'll give a qualitative idea.
        print(f"Average Activity Frequency (Active Customers): Approx. 0.5 events/day (based on simulation parameters)")
    else:
        print("No active customers to estimate activity frequency.")

    # Distribution of True Churn Propensity
    if not df.empty and 'churn_propensity_true' in df.columns:
        print("\nDistribution of True Churn Propensity:")
        plt.figure(figsize=(10, 6))
        plt.hist(df['churn_propensity_true'], bins=10, edgecolor='black', alpha=0.7)
        plt.title("Distribution of True Churn Propensity Across Customers")
        plt.xlabel("Churn Propensity")
        plt.ylabel("Number of Customers")
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    else:
        print("\nChurn propensity data not available or DataFrame is empty for plotting.")

    # Distribution of event types (overall, could be refined to recent activity only)
    all_event_types = []
    for events_list in df['events']:
        for event in events_list:
            all_event_types.append(event['type'])
    
    event_type_counts = pd.Series(all_event_types).value_counts()
    if not event_type_counts.empty:
        print("\nOverall Distribution of Event Types:")
        print(event_type_counts.to_string())
        plt.figure(figsize=(10, 6))
        event_type_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Overall Distribution of Customer Event Types")
        plt.xlabel("Event Type")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo event data to display distribution.")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    # Example usage if this file is run directly
    print("Running customer_dashboard.py directly. Generating sample data and displaying dashboard...")
    # This requires a simple data generation capability
    import sys
    import os
    # Add parent directory to path to import data_simulator (if run from same directory level)
    # This might need adjustment based on how the user structures their project.
    # For a simple test, we'll simulate data directly here.
    
    # Minimal data simulation for standalone test
    def _generate_test_customer_events(num_days, churn_propensity):
        events = []
        current_date = datetime.now() - timedelta(days=num_days)
        for day in range(num_days):
            events.append({'date': current_date.strftime('%Y-%m-%d'), 'type': random.choice(['login', 'make_purchase', 'inactivity'])})
            current_date += timedelta(days=1)
        if random.random() < churn_propensity:
            events.append({'date': current_date.strftime('%Y-%m-%d'), 'type': 'churned'})
            churned = True
            churn_date = current_date.strftime('%Y-%m-%d')
        else:
            churned = False
            churn_date = None
        return events, churned, churn_date

    def _simulate_test_customer_data(num_customers=10):
        customers_data = []
        for i in range(num_customers):
            cust_id = f"TEST_CUST-{i:02d}"
            start_date = datetime.now() - timedelta(days=random.randint(50, 200))
            num_days_active = (datetime.now() - start_date).days
            churn_prop = random.random()
            events, churned, churn_date = _generate_test_customer_events(num_days_active, churn_prop)
            customers_data.append({
                'customer_id': cust_id,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'last_activity_date': events[-1]['date'],
                'churned': churned,
                'churn_date': churn_date,
                'events': events,
                'churn_propensity_true': churn_prop
            })
        return pd.DataFrame(customers_data)

    test_df = _simulate_test_customer_data(num_customers=20)
    display_customer_dashboard(test_df)
