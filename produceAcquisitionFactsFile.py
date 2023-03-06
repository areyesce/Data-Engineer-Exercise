import pandas as pd

people_info = pd.read_csv("people.csv")

# print(people_info.info())
# print(people_info.head(10))

people_info['created_dt'] = pd.to_datetime(people_info['created_dt']).dt.date
# print(people_info.head(10))

""" sorted for easy plotting """
val_counts_df = people_info['created_dt'].value_counts().rename_axis('acquisition_date').reset_index(name='acquisitions').sort_values(by='acquisition_date').reset_index(drop=True)

# print(val_counts_df.info())
# print(val_counts_df)

val_counts_df.to_csv("acquisition_facts.csv", index=False)


