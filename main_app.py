import random
import matplotlib.pyplot as plt
import pandas as pd # Needed for DataFrame operations when passing data around

# Import functions from our custom modules
from data_simulator import simulate_customer_data
from churn_model import monte_carlo_churn_prediction
from intervention_strategy import suggest_intervention
from customer_dashboard import display_customer_dashboard

# --- Configuration (for consistent results) ---
random.seed(42)
np.random.seed(42) # NumPy needed by churn_model, so import here too for consistency if not within functions


def main():
    """
    Main function to run the customer churn prediction and dashboard application in Colab.
    Provides a menu-driven interface for user interaction.
    """
    print("--- Customer Churn Prediction & Intervention (Colab Version) ---")
    print("This script simulates customer behavior, predicts churn risk using Monte Carlo simulation,")
    print("and provides a customer health dashboard.")
    print("-" * 70)

    # Generate or load data once at the start of the application
    print("Generating synthetic customer data...")
    df_customers = simulate_customer_data(num_customers=50)
    print(f"Generated {len(df_customers)} customers.")

    while True:
        print("\n--- Main Menu ---")
        print("1. View Customer Health Dashboard (Overall Metrics)")
        print("2. Analyze Individual Customer Churn (Prediction & Intervention)")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Pass a copy of the DataFrame to the dashboard function
            # to prevent any unintended modifications to the original df_customers.
            display_customer_dashboard(df_customers.copy())
        
        elif choice == '2':
            # Logic for analyzing individual customer churn
            print("\n--- Individual Customer Analysis ---")
            print("Available Customers:")
            for i, cust_id in enumerate(df_customers['customer_id'].tolist()):
                print(f"  {i+1}. {cust_id}")

            selected_customer = None
            while selected_customer is None:
                try:
                    selection_input = input("Enter the number of the customer to analyze (e.g., 1, 2, ...): ")
                    selected_index = int(selection_input) - 1
                    if 0 <= selected_index < len(df_customers):
                        selected_customer = df_customers.iloc[selected_index]
                    else:
                        print("Invalid number. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            selected_customer_id = selected_customer['customer_id']
            print(f"\nAnalyzing Customer: {selected_customer_id}")
            print("-" * 70)

            print("\n--- Customer Overview ---")
            print(f"Start Date: {selected_customer['start_date']}")
            print(f"Last Activity Date: {selected_customer['last_activity_date']}")
            if selected_customer['churned']:
                print(f"Status: CHURNED on {selected_customer['churn_date']}")
            else:
                print("Status: Active")
            print(f"(True Churn Propensity: {selected_customer['churn_propensity_true']:.2f})")

            print("\n--- Recent Customer Activity ---")
            event_df = pd.DataFrame(selected_customer['events'])
            if not event_df.empty:
                print(event_df.tail(10).to_string()) # Display recent events
            else:
                print("No recent activity recorded for this customer.")

            print("\n--- Churn Prediction using Monte Carlo Simulation ---")
            input("Press Enter to predict churn risk (this will run Monte Carlo simulations)...")

            print("Running Monte Carlo Simulations for churn prediction...")
            # Note: monte_carlo_churn_prediction expects a dict-like customer_data
            mean_churn_prob, std_churn_prob, all_probs = monte_carlo_churn_prediction(selected_customer.to_dict())

            print("\n--- Prediction Results ---")
            print(f"Predicted Churn Probability (Mean): {mean_churn_prob:.2f}")
            print(f"Standard Deviation of Predictions (from MC): {std_churn_prob:.2f}")

            # Visualize distribution of probabilities
            print("\nDisplaying distribution of Churn Probabilities from Monte Carlo Simulations...")
            plt.figure(figsize=(10, 6))
            plt.hist(all_probs, bins=10, edgecolor='black', alpha=0.7)
            plt.title("Monte Carlo Churn Probability Distribution")
            plt.xlabel("Churn Probability")
            plt.ylabel("Frequency")
            plt.grid(axis='y', alpha=0.75)
            plt.show()

            print("\n--- Suggested Intervention Strategy ---")
            intervention = suggest_intervention(mean_churn_prob)
            print(f"Title: {intervention['title']}")
            print(f"Description: {intervention['description']}")
            print("Recommended Actions:")
            for action in intervention['actions']:
                print(f"- {action}")
            
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n" + "=" * 70)
    print("Disclaimer: This is a simplified simulation for demonstration purposes. Real-world churn prediction requires complex models, extensive data, and validation.")
    print("=" * 70)

if __name__ == '__main__':
    main()