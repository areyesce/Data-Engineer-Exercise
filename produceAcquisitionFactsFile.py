import pandas as pd

people_info = pd.read_csv("people.csv")

"""" shorten the timestamp to only include the date field of the object """
people_info['created_dt'] = pd.to_datetime(people_info['created_dt']).dt.date

""" sorted for easy plotting """
val_counts_df = people_info['created_dt'].value_counts().rename_axis('acquisition_date').reset_index(name='acquisitions').sort_values(by='acquisition_date').reset_index(drop=True)

val_counts_df.to_csv("acquisition_facts.csv", index=False)


