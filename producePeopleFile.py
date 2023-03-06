import pandas as pd

const_info = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv") 
const_emails = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv") 
const_sub_status = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv")

"""
Produce a “people” file with the following schema. 
* We only care about subscription statuses where chapter_id is 1. *
"""

""" dataframe with entries where chapter_id is 1 from Constituent Subscription Status"""
chapter_id_1_rows = const_sub_status.loc[const_sub_status['chapter_id'] == 1]
# print(chapter_id_1_rows.info())
# total number of entries where chapter_id is 1, 275484/350000

""" save list of cons_email_id values """
cons_email_id_list = chapter_id_1_rows['cons_email_id'].to_list()
# print(chapter_id_1_rows['cons_email_id'].value_counts()) 
# verified cons_email_id values are unique

""" filter entries from Constituent Email Addresses that are in cons_email_id_list and are primary email """

const_emails_primary = const_emails[(const_emails.cons_email_id.isin(cons_email_id_list)) & (const_emails.is_primary == 1)]
# print(const_emails_primary.info())
# 173990/275484 entries where is_primary = 1

""" sort primary list by cons_email_id """
const_emails_primary_sorted = const_emails_primary.sort_values(by='cons_email_id')

""" save list of cons_email_id values """
cons_email_id_list_from_primary = const_emails_primary_sorted['cons_email_id'].to_list()


""" filter entries from Constituent Subscription Status that are in saved list of cons_email_id's """
isunsub_df = const_sub_status[const_sub_status.cons_email_id.isin(cons_email_id_list_from_primary)]

# print(isunsub_df.info())
"""
NOTE: df sizes # entries did not match, after dropping duplicates 134259 entries remained
"""
isunsub_df_sorted = isunsub_df.sort_values(by='cons_email_id')
isunsub_df_sorted.drop_duplicates(subset='cons_email_id',keep=False, inplace=True)
# print(isunsub_df_sorted.info()) # 134259 entries

""" drop all columns except 'cons_email_id' and 'isunsub' to perform a left outer join 
to const_emails_primary_sorted['cons_email_id','email'] to keep all primary emails 
even if primary email has no matching isunsub status """
isunsub_by_cons_email_id = isunsub_df_sorted.drop(['cons_email_chapter_subscription_id','chapter_id','unsub_dt','modified_dt'], axis=1)


""" perform left outer join based on shared 'cons_email_id' column 
    LEFT: const_emails_primary_sorted['cons_email_id','email','cons_id']
    RIGHT: const_sub_status['cons_email_id','isunsub']
    RESULT: const_emails_primary_sorted['cons_email_id','email','cons_id','isunsub']
"""
emails_by_cons_email_id = const_emails_primary_sorted[['cons_email_id','email','cons_id']]
output = pd.merge(emails_by_cons_email_id, isunsub_by_cons_email_id, on='cons_email_id', how='left')

""" source, person created and updated info columns are drawn from Constituent Information dataset 
    to match to rows in output df (derived by subset of entries with primary email) using 'cons_id' 
"""

""" create subset of Constituent Info with source, create_dt, and modified_dt columns """
const_info_sub = const_info[['cons_id','source','create_dt','modified_dt']]

""" use const_info_sub set to perform a left outer join to output df, 
    which is sorted by primary emails; join on cons_id 
    LEFT: const_emails_primary_sorted['cons_email_id','email','cons_id','isunsub']
    RIGHT: const_info['cons_id','source','create_dt','modified_dt']
    RESULT: const_emails_primary_sorted['cons_email_id','email','cons_id','isunsub','source','create_dt','modified_dt'] 
"""
final_output = pd.merge(output,const_info_sub, on='cons_id', how='left')

""" drop cons_email_id and cons_id columns before saving to csv file """
final_output_dropped_ids = final_output[['email','source','isunsub','create_dt','modified_dt']]

headerList = ['email','code','is_unsub','created_dt','updated_dt']

final_output_dropped_ids.to_csv("people.csv", header=headerList, index=False)

view_file = pd.read_csv("people.csv")

print(view_file)








