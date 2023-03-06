# Data-Engineer-Exercise

The following documentation describes how to run this app locally. First install dependencies, then use terminal to execute python scripts.


## Install the following dependencies
* install python3 
* pip3 install pandas

## Run app locally
#### In a terminal inside the working directory type:
* python3 producePeopleFile.py
  * creates 'people.csv' file
* python3 produceAcquisitionFactsFile.py
  * creates 'acquisition_facts.csv'; can only execute this line after creating 'people.csv' in previous step


## Program outputs:

#### 1) Produce a “people” file with the following schema. Save it as a CSV with a header line to the working directory.


| Column | Type | Description |
| -------| -----| ------ |
| email | string| Primary email address |
| code | string| Source code |
| is_unsub | boolean| Is the primary email address unsubscribed? |
| created_dt | datetime | Person creation datetime |
| updated_dt | datetime | Person updated datetime |

#### 2) Use the output of #1 to produce an “acquisition_facts” file with the following schema that aggregates stats about when people in the dataset were acquired. Save it to the working directory.


| Column | Type | Description |
| -------| -----| ------ |
| acquisition_date | date| Calendar date of acquisition |
| acquisitions | int| Number of constituents acquired on acquisition_date |


#### Datasets

A dataset simulating CRM data is available in some public AWS S3 files:
* Constituent Information: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv
* Constituent Email Addresses: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv
  * Boolean columns (including is_primary) in all of these datasets are 1/0 numeric values. 1 means True, 0 means False.
* Constituent Subscription Status: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv
  * We only care about subscription statuses where chapter_id is 1.
  * If an email is not present in this table, it is assumed to still be subscribed where chapter_id is 1.






















