import pandas as pd

def analyze_pareto_rotation(df):
    """
    Identifies fleet rotation concentration (Vital Few vs. Trivial Many).
    Project Reference: LOG-STRAT-001
    Methodology: Pareto 80-20 Rule.
    """
    
    # 1. Group rotations by Truck ID (License Plate) and sort descending
    # Based on the finding that 50% of trucks drive 80% of volume [cite: 128, 129]
    rotation_data = df.groupby('plate_id')['rotations'].sum().reset_index()
    rotation_data = rotation_data.sort_values(by='rotations', ascending=False)
    
    # 2. Calculate cumulative percentages
    total_rotations = rotation_data['rotations'].sum()
    rotation_data['cumulative_sum'] = rotation_data['rotations'].cumsum()
    rotation_data['cumulative_perc'] = 100 * (rotation_data['cumulative_sum'] / total_rotations)
    
    # 3. Identify the "Vital Few" (The units representing 80% of the operation)
    vital_few = rotation_data[rotation_data['cumulative_perc'] <= 81] # Margin for 80% cut-off
    
    # 4. Impact Reporting
    fleet_size = len(rotation_data)
    vital_few_size = len(vital_few)
    concentration_ratio = (vital_few_size / fleet_size) * 100
    
    print(f"--- LOG-STRAT-001: Pareto Distribution Analysis ---")
    print(f"Total Fleet Size: {fleet_size} units")
    print(f"Vital Few: {vital_few_size} units represent 80% of the total rotation.")
    print(f"Concentration Ratio: {concentration_ratio:.2f}% of the fleet handles the core volume.")
    
    return rotation_data

# --- Unit Test / Implementation Example ---
if __name__ == "__main__":
    # Simulated data reflecting the 2021-2022 logistics study [cite: 127]
    data = {
        'plate_id': ['TRUCK-01', 'TRUCK-02', 'TRUCK-03', 'TRUCK-04', 'TRUCK-05', 'TRUCK-06'],
        'rotations': [45, 38, 30, 10, 5, 2] # Clearly concentrated volume
    }
    sample_df = pd.DataFrame(data)
    analyze_pareto_rotation(sample_df)
