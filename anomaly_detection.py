import numpy as np
import matplotlib.pyplot as plt
import time

# Function to calculate Exponential Moving Average (EMA)
def update_ema(current_ema, new_value, alpha=0.1):
    """
    Update the Exponential Moving Average (EMA) with a new data point.

    Parameters:
    - current_ema: The current EMA value.
    - new_value: The new data point to include in the EMA calculation.
    - alpha: The smoothing factor (0 < alpha < 1).

    Returns:
    - The updated EMA value.
    """
    return alpha * new_value + (1 - alpha) * current_ema

# Function to detect anomalies (based on deviation from EMA)
def detect_anomaly(value, ema, threshold=1):
    """
    Detect anomalies based on the deviation from the Exponential Moving Average (EMA).

    Parameters:
    - value: The current data point.
    - ema: The current EMA value.
    - threshold: The deviation threshold for anomaly detection.

    Returns:
    - True if the value is an anomaly, otherwise False.
    """
    return abs(value - ema) > threshold

# Simulate data stream function
def generate_data_stream():
    """
    Generate a continuous data stream of sine wave values with added noise.

    Yields:
    - A new data point representing the current value in the data stream.
    """
    while True:
        value = np.sin(time.time()) + np.random.normal(0, 0.5)  # Increased noise for more variation
        yield value

# Visualization setup
plt.ion()  # Interactive mode ON
fig, ax = plt.subplots()
x, y, anomalies = [], [], []

# Set initial EMA value (start with the first value in the stream)
data_stream = generate_data_stream()
first_value = next(data_stream)
ema = first_value  # Initialize EMA with the first value

# Simulate data stream and plot with anomaly detection
for i in range(100):  # Example: Run for 100 iterations
    new_value = next(data_stream)  # Get next value from data stream
    
    # Update EMA with new data point
    ema = update_ema(ema, new_value)
    
    # Check for anomalies
    is_anomaly = detect_anomaly(new_value, ema)
    
    # Add new data points
    x.append(i)
    y.append(new_value)
    anomalies.append(new_value if is_anomaly else None)  # Mark anomaly
    
    # Plot data stream and anomalies
    ax.clear()
    ax.plot(x, y, label="Data Stream")
    
    # Highlight anomalies in red
    if any(anomalies):
        ax.scatter(x, anomalies, color='red', label="Anomalies")
    
    ax.legend()
    plt.pause(0.05)  # Pause for visualization

# Stop interactive mode
plt.ioff()
plt.show()

