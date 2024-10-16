# Efficient Data Stream Anomaly Detection

## Project Description
This project simulates a real-time data stream and detects anomalies using an Exponential Moving Average (EMA) algorithm. It is designed to identify unusual patterns in metrics such as financial transactions or system performance data.

## Features
- Real-time anomaly detection in continuous data streams.
- Exponential Moving Average (EMA) based anomaly detection.
- Visualization of data stream and detected anomalies.

## How to Run
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt

## Usage Example
After running the script, you should see a real-time plot of the data stream with detected anomalies marked as red dots. The anomalies are flagged based on deviations from the Exponential Moving Average.


### Algorithm Explanation
- This project uses the Exponential Moving Average (EMA) to smooth data and identify deviations. The EMA reacts faster to recent changes, allowing for effective anomaly detection in dynamic streams. Anomalies are flagged when a value deviates from the EMA by more than a set threshold.

### Requirements
Python 3.x
numpy
matplotlib




