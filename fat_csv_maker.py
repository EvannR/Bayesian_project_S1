import pandas as pd
import numpy as np
import os


"""
To make this program work you have to call and change the values : 
def generate_data_CDF(Stest_std=0, 
                      Stest_range_min=-4, 
                      Stest_range_max=4, 
                      Sref_mean=0, 
                      Sref_std=0,
                      number_repetition_per_trial=50, 
                      step_change_Stest=0.25):


"""

def generate_dataframe():
    """Generate an empty dataframe with predefined columns."""
    columns = ['Trial', 'Stimulus 1 Value', 'Stimulus 1 Std', 'Stimulus 2 Value', 'Stimulus 2 Std']
    return pd.DataFrame(columns=columns)


def trial_maker(number_repetition_per_trial, step_change_Stest, Sref, Stest_range_min, Stest_range_max, std_Stest, std_Sref):
    """
    Generate a DataFrame containing experimental trials.

    Parameters:
    - number_repetition_per_trial: int, repetitions per trial.
    - step_change_Stest: float, increment step for stimulus test value.
    - Sref: float, reference stimulus value.
    - Stest_range_min: float, minimum value for stimulus test range.
    - Stest_range_max: float, maximum value for stimulus test range.
    - std_Stest: float, standard deviation for stimulus test.
    - std_Sref: float, standard deviation for reference stimulus.

    Returns:
    - df: DataFrame containing the generated trials.
    """
    data = []
    trial_id = 1

    for value_stimulus_test in np.arange(Stest_range_min, Stest_range_max + step_change_Stest, step_change_Stest):
        for _ in range(number_repetition_per_trial):
            data.append({
                'Trial': trial_id,
                'Stimulus 1 Value': value_stimulus_test,
                'Stimulus 1 Std': std_Stest,
                'Stimulus 2 Value': Sref,
                'Stimulus 2 Std': std_Sref
            })
            trial_id += 1

    return pd.DataFrame(data)


def generate_data_CDF(Stest_std=0, 
                      Stest_range_min=-4, 
                      Stest_range_max=4, 
                      Sref_mean=0, 
                      Sref_std=0,
                      number_repetition_per_trial=50, 
                      step_change_Stest=0.25):
    """
    Generate data for experimental trials and save to a CSV file. Logs generation parameters.

    Parameters:
    - Stest_std, Stest_range_min, Stest_range_max, Sref_mean, Sref_std: float
    - number_repetition_per_trial: int
    - step_change_Stest: float
    """
    # Create directory for experiment data if not exists
    folder_name = "experiment_1_data_cdf"
    os.makedirs(folder_name, exist_ok=True)
    combined_file_path = os.path.join(folder_name, "data_cdf_combined.csv")
    log_file_path = os.path.join(folder_name, "data_generation_log.txt")

    # Generate trials data
    df = trial_maker(
        number_repetition_per_trial=number_repetition_per_trial,
        step_change_Stest=step_change_Stest,
        Sref=Sref_mean,
        Stest_range_min=Stest_range_min,
        Stest_range_max=Stest_range_max,
        std_Stest=Stest_std,
        std_Sref=Sref_std
    )

    # Append data to CSV
    if os.path.exists(combined_file_path):
        df.to_csv(combined_file_path, mode='a', index=False, header=False)
    else:
        df.to_csv(combined_file_path, index=False, header=True)

    # Log parameters
    num_rows_added = len(df)
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"New data added: {num_rows_added} rows\n")
        log_file.write(f"Stest_std: {Stest_std}, Stest_range_min: {Stest_range_min}, "
                       f"Stest_range_max: {Stest_range_max}, Sref_mean: {Sref_mean}, "
                       f"Sref_std: {Sref_std}, number_repetition_per_trial: {number_repetition_per_trial}, "
                       f"step_change_Stest: {step_change_Stest}\n")
        log_file.write("-" * 50 + "\n")
