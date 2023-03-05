import pandas as pd

# making data frame 
const_info = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv") 
const_emails = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv") 
const_sub_status = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv")

# const_info_top = const_info.head() 
# print(const_info_top)
# print(list(const_info.columns))
# print(const_info.info()) # 700000 entries

# const_emails_top = const_emails.head(10) 
# print(const_emails_top)
# print(list(const_emails.columns))
# print(const_emails.info()) # 1400000 entries

# const_sub_status_top = const_sub_status.head(10)
# print(const_sub_status_top)
# print(list(const_sub_status.columns))
# print(const_sub_status.info()) # 350000 entries

"""
Produce a “people” file with the following schema. 
TODO: Save it as a CSV with a header line to the working directory.
* We only care about subscription statuses where chapter_id is 1. *
"""
# total number of entries where chapter_id is 1, 275484/350000
# print(len(const_sub_status[const_sub_status['chapter_id']==1]))

"""df with entries where chapter_id is 1"""
chapter_id_1_rows = const_sub_status.loc[const_sub_status['chapter_id'] == 1]
"""TODO: may need to reset index"""
# print(chapter_id_1_rows.info())
# print(chapter_id_1_rows.head(10))

"""TODO: ADD HEADER TO CSV CREATED"""

""" save list of cons_email_id values """
cons_email_id_list = chapter_id_1_rows['cons_email_id'].to_list()
# print("cons email list") 
# print(cons_email_id_list)
# print(chapter_id_1_rows['cons_email_id'].value_counts()) # unique

""" get rows from const emails df that are in cons_email_id_list and are primary email """
""" 173990/275484 were is_primary """
const_emails_primary = const_emails[(const_emails.cons_email_id.isin(cons_email_id_list)) & (const_emails.is_primary == 1)]

# print(const_emails_primary.info())
# print(const_emails_primary.head(10))

""" from here could choose to just drop columns and then merge from third file """
""" sort primary list by cons_email_id """
const_emails_primary_sorted = const_emails_primary.sort_values(by='cons_email_id')
print(const_emails_primary_sorted.info())
print(const_emails_primary_sorted.head(10))

""" save list of cons_email_id values MIGHT NOT NEED THESE """
cons_email_id_list_from_primary = const_emails_primary_sorted['cons_email_id'].to_list()
# print(cons_email_id_list_from_primary)

cons_email_id_set = set(cons_email_id_list_from_primary)
# print("Set: ",cons_email_id_set)

isunsub_df = const_sub_status[const_sub_status.cons_email_id.isin(cons_email_id_list_from_primary)]
# print(isunsub_df.info())
# print(isunsub_df.head(10))

"""
NOTE: df sizes # entries do not match, after drop duplicates remains 134259 entries
"""
isunsub_df_sorted = isunsub_df.sort_values(by='cons_email_id')
isunsub_df_sorted.drop_duplicates(subset='cons_email_id',keep=False, inplace=True)
# print(isunsub_df_sorted.info()) # 134259 entries
# print(isunsub_df_sorted.head(10))

""" drop all columns except cons_email_id and isunsub to perform a left outer join 
to const_emails_primary_sorted['cons_email_id','email'] to keep all primary emails 
even if no isunsub status """
isunsub_by_cons_email_id = isunsub_df_sorted.drop(['cons_email_chapter_subscription_id','chapter_id','unsub_dt','modified_dt'], axis=1)
# print(isunsub_by_cons_email_id.info())
# print(isunsub_by_cons_email_id.head(10))


""" sort by cons_email_id before joining"""

# test_None_col = [None,None,1]
# test_df = pd.DataFrame({"NoneTest":test_None_col})
# print(test)

emails_by_cons_email_id = const_emails_primary_sorted[['cons_email_id','email','cons_id']]
output = pd.merge(emails_by_cons_email_id, isunsub_by_cons_email_id, on='cons_email_id', how='left')
print(output.info())
print(output.head(10))






