import pandas as pd

input_path = r"C:\Users\echan\Downloads\Medicare_Part_D_Prescribers_by_Provider_and_Drug_2024\Medicare_Part_D_Prescribers_by_Provider_and_Drug_2024.csv"
output_path = "part_d_california.csv"

state_to_keep = "CA"
first_chunk = True

for chunk in pd.read_csv(input_path, chunksize=500_000):
    filtered = chunk[chunk["Prscrbr_State_Abrvtn"] == state_to_keep]
    filtered.to_csv(output_path, mode="a", index=False, header=first_chunk)
    first_chunk = False

print("Done! Filtered file saved.")