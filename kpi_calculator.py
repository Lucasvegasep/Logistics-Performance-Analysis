import pandas as pd
import numpy as np

def calculate_logistics_kpis(df):
    """
    Automated Engine for Logistics KPI Calculation.
    Project Reference: LOG-STRAT-001
    Focus: Operational Friction & Cycle Time Optimization.
    """
    
    # 1. Configuration: Operational Efficiency Threshold
    # As per LOG-STRAT-001, the target stay time is 2.5 hours.
    target_time_hours = 2.5
    
    # 2. Pre-processing: Calculate Stay Time (In-Plant Cycle)
    # Ensures data is treated as datetime for temporal precision.
    df['arrival'] = pd.to_datetime(df['arrival'])
    df['departure'] = pd.to_datetime(df['departure'])
    
    # Calculation of total hours in plant
    df['stay_time_hrs'] = (df['departure'] - df['arrival']).dt.total_seconds() / 3600
    
    # 3. KPI: Operational Friction Index
    # Measures the percentage of the fleet operating outside the efficiency window.
    over_target = df[df['stay_time_hrs'] > target_time_hours]
    friction_index = (len(over_target) / len(df)) * 100
    
    # 4. KPI: Fleet Average Stay Time
    # Core metric for baseline performance tracking.
    avg_stay = df['stay_time_hrs'].mean()
    
    # 5. Output Reporting
    print(f"--- LOG-STRAT-001: Operational Excellence Report ---")
    print(f"Friction Index (> {target_time_hours}h): {friction_index:.2f}%")
    print(f"Average Fleet Stay Time: {avg_stay:.2f} hours")
    
    return {
        "friction_index": friction_index,
        "average_stay_time": avg_stay
    }

# --- Unit Test / Implementation Example ---
if __name__ == "__main__":
    # Simulated logistics data for demonstration
    data = {
        'arrival': ['2026-04-27 08:00:00', '2026-04-27 09:30:00', '2026-04-27 10:00:00'],
        'departure': ['2026-04-27 10:15:00', '2026-04-27 13:00:00', '2026-04-27 12:00:00']
    }
    sample_df = pd.DataFrame(data)
    calculate_logistics_kpis(sample_df)
