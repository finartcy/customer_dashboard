Customer Churn Prediction and Health Dashboard
This project provides a simulated customer churn prediction system using Monte Carlo simulations and a customer health dashboard. It's designed for demonstration and educational purposes, illustrating key concepts in customer analytics.

Table of Contents
Features

Project Structure

Python Package Dependencies

Installation and Setup

Usage

Running in Google Colab

Running Locally (Production Environment)

Disclaimer

License

Features
Simulated Customer Data: Generates realistic synthetic customer activity data, including login, purchases, support queries, and simulated churn events.

Simplified Churn Prediction Model: Uses a "Recurrent Neural Network"-like logic to assess churn risk based on recent customer activity patterns.

Monte Carlo Churn Simulation: Employs Monte Carlo methods to forecast future churn probabilities, providing a more robust prediction and confidence interval.

Churn Intervention Strategy: Suggests actionable interventions (High, Moderate, Low risk) based on predicted churn probability.

Customer Health Dashboard: Quantifies key metrics for overall customer health, including churn rate, average tenure, and event distribution.

Modular Design: Code is organized into separate modules for better maintainability and reusability.

Project Structure
customer_churn_project/
├── __init__.py
├── data_simulator.py
├── churn_model.py
├── intervention_strategy.py
├── customer_dashboard.py
└── main_app.py

__init__.py: Marks the directory as a Python package.

data_simulator.py: Handles the generation of synthetic customer data and event streams.

churn_model.py: Contains the simplified churn prediction logic and the Monte Carlo simulation.

intervention_strategy.py: Defines the rules for suggesting customer interventions based on churn probability.

customer_dashboard.py: Provides functions to display aggregate customer health metrics and visualizations.

main_app.py: The main entry point for the application, orchestrating the calls to other modules and handling user interaction.

Python Package Dependencies
This project requires the following Python packages:

pandas

numpy

matplotlib

You can install these dependencies using pip:

pip install pandas numpy matplotlib

Installation and Setup
Running in Google Colab
Create a folder: In your Google Drive, create a new folder, e.g., customer_churn_project.

Create __init__.py: Inside customer_churn_project, create an empty file named __init__.py.

Upload Python files: Upload all .py files (from the Project Structure section) into the customer_churn_project folder in your Google Drive.

Open Colab and Run:

Open a new Google Colab notebook.

Mount your Google Drive:

from google.colab import drive
drive.mount('/content/drive')

Navigate to your project directory:

# Adjust the path below to where you uploaded your folder
%cd /content/drive/My Drive/customer_churn_project/

Install dependencies:

!pip install pandas numpy matplotlib

Run the main application:

%run main_app.py

Running Locally (Production Environment)
Clone the repository:

git clone https://github.com/your-username/customer_churn_project.git
cd customer_churn_project

(Note: Replace https://github.com/your-username/customer_churn_project.git with the actual URL of your GitHub repository once created.)

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

(You'll need to create a requirements.txt file first if you don't have one. You can generate it after installing dependencies with pip freeze > requirements.txt)

Run the application:

python main_app.py

Usage
Once the main_app.py script is running, it will present a text-based menu in your terminal (or Colab output). You can choose to:

View Customer Health Dashboard: See aggregate metrics and visualizations for all simulated customers.

Analyze Individual Customer Churn: Select a specific customer, view their details, predict their churn probability using Monte Carlo, and get intervention suggestions.

Follow the on-screen prompts to interact with the application.

Disclaimer
This project is a simplified simulation for demonstration and educational purposes. The "Weibull-time-to-event Recurrent neural network" and "Quantum Optimization" aspects are simulated in their conceptual outcomes and do not represent full-scale, computationally intensive implementations. Real-world customer churn prediction and optimization require complex models, extensive and validated data, and robust statistical methods beyond the scope of this demonstration.

License
This project is licensed under the MIT License, with an additional clause requiring attribution.

MIT License

Copyright (c) [Year] [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Special Attribution Clause:

Notwithstanding any other provision of this License, any direct or indirect use, reproduction, modification, distribution, or public display of this Software, or any derivative works thereof, must prominently acknowledge Gerald Maurice Thomas as the original creator. This acknowledgement should be made in a clear and conspicuous manner within the product, documentation, or associated materials.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.