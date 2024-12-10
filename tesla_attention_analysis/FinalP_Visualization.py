import pandas as pd
import matplotlib.pyplot as plt

def visualize(combined_data):
# Reload the combined dataset
    combined_data = pd.read_csv('Final_tesla_combined_weekly_data.csv')

    # Ensure the 'Week' column is in datetime format for proper plotting
    combined_data['Week'] = pd.to_datetime(combined_data['Week'])

    # Calculate the weekly percentage change in stock price
    combined_data['Weekly % Change'] = combined_data['Weekly Stock Price'].pct_change() * 100

    # Drop the first row (NaN value from pct_change)
    combined_data.dropna(subset=['Weekly % Change'], inplace=True)

    # Create the figure and axis
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Google Trends Attention on the left y-axis
    ax1.plot(combined_data['Week'], combined_data['Google Trends Attention'], color='blue', label='Google Trends Attention')
    ax1.set_xlabel('Time (Week)')
    ax1.set_ylabel('Google Trends Attention', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create the second y-axis for Stock Price
    ax2 = ax1.twinx()
    ax2.plot(combined_data['Week'], combined_data['Weekly Stock Price'], color='green', label='Stock Price')
    ax2.set_ylabel('Stock Price (USD)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Add title and legend
    plt.title('Tesla Weekly Google Trends Attention and Stock Price')
    fig.tight_layout()  # Adjust layout to prevent overlap
    plt.show()










    # Create the figure and axis
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Google Trends Attention on the left y-axis
    ax1.plot(combined_data['Week'], combined_data['Google Trends Attention'], color='blue', label='Google Trends Attention')
    ax1.set_xlabel('Time (Week)')
    ax1.set_ylabel('Google Trends Attention', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create the second y-axis for Stock Price
    ax2 = ax1.twinx()
    ax2.plot(combined_data['Week'], combined_data['Weekly % Change'], color='green', label='% Change')
    ax2.set_ylabel('Stock Price (USD)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Add title and legend
    plt.title('Tesla Stock Weekly % Change and Google Trends Attention Over Time')
    fig.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
