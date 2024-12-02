import numpy as np
import os
import csv

def generate_data_CDF(Stest_std=0,
                      Stest_range_min=-4, 
                      Stest_range_max=4,
                      Sref_mean=0,
                      Sref_std=0,
                      number_repetition_per_trial=50, 
                      step_change_Stest=0.25,
                      ):
    '''
    Fonction qui génère directement un fichier CSV avec les données de simulation.
    '''
    # Vérifiez ou créez le dossier "experiment_1_data_cdf"
    folder_name = "experiment_1_data_cdf"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Définissez le chemin complet du fichier
    file_name = f"data-cdf_{Stest_range_min}-{Stest_range_max}_{Stest_std}_{Sref_mean}_{Sref_std}.csv"
    file_path = os.path.join(folder_name, file_name)
    
    # Définissez les colonnes
    columns = ['Trial', 'Stimulus 1 Value', 'Stimulus 1 Std', 'Stimulus 2 Value', 'Stimulus 2 Std']
    
    # Ouvrez le fichier en mode écriture
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)  # Écrivez l'en-tête

        trial_number = 1
        # Générez les données ligne par ligne
        for value_stimulus_test in np.arange(Stest_range_min, Stest_range_max + step_change_Stest, step_change_Stest):
            for _ in range(number_repetition_per_trial):
                writer.writerow([
                    trial_number,
                    value_stimulus_test,
                    Stest_std,
                    Sref_mean,
                    Sref_std
                ])
            trial_number += 1
