import pandas as pd

# making data frame 
# const_info = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv") 
# const_emails = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv") 
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
"""
# total number of entries where chapter_id is 1, 275484/350000
# print(len(const_sub_status[const_sub_status['chapter_id']==1]))

chapter_id_1_rows = const_sub_status.loc[const_sub_status['chapter_id'] == 1]
"""TODO: may need to reset index"""
print(chapter_id_1_rows.info())
print(chapter_id_1_rows.head(10))




