import pandas as pd
import numpy as np


def generate_dataframe():
    columns = ['Trial',
               'Stimulus 1 Value',
               'Stimulus 1 Std',
               'Stimulus 2 Value',
               'Stimulus 2 Std']
    df = pd.DataFrame(columns=columns)
    return df


def trial_maker(number_repetition_per_trial,
                step_change_Stest, Sref,
                Stest_range_min,
                Stest_range_max,
                std_Stest, std_Sref):
    """
    Generate the dataframe with the experimental trials.
    """
    df = generate_dataframe()
    number_row = 1

    for value_stimulus_test in np.arange(Stest_range_min,
                                         Stest_range_max + step_change_Stest,
                                         step_change_Stest):
        for repetition in range(number_repetition_per_trial):
            new_row = {
                'Trial': int(number_row),
                'Stimulus 1 Value': float(value_stimulus_test),
                'Stimulus 1 Std': float(std_Stest),
                'Stimulus 2 Value': float(Sref),
                'Stimulus 2 Std': float(std_Sref)
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            number_row += 1

    return df


def generate_data_CDF(Sref_mean, Stest_std,
                      number_repetition_per_trial=10, step_change_Stest=0.25,
                      Stest_range_min=-4, Stest_range_max=4, std_Sref=0):
    '''
    Function that call the constructor of dataframe to create a csv.
    changing its parameter by default changes the parameter of simulations
    '''
    df = trial_maker(
        number_repetition_per_trial=number_repetition_per_trial,
        step_change_Stest=step_change_Stest,
        Sref=Sref_mean,
        Stest_range_min=Stest_range_min,
        Stest_range_max=Stest_range_max,
        std_Stest=Stest_std,
        std_Sref=std_Sref
    )

    file_name = f"data_cdf_{Sref_mean}_{Stest_std}.csv"
    df.to_csv(file_name, index=False)
    print(f"DataFrame sauvegardé dans {file_name}")


generate_data_CDF(0, 2)
