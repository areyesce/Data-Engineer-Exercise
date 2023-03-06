# MissionWired Data-Engineer-Exercise

The following documentation describes how to run this app locally. First install dependencies, then use terminal to execute python scripts.


## Install the following dependencies: 
* install python3 
* pip3 install pandas

## Run app locally, in terminal type:
* python3 producePeopleFile.py
  * creates 'people.csv' file
* python3 produceAcquisitionFactsFile.py
  * creates 'acquisition_facts.csv'; can only execute this line after creating 'people.csv' in previous step


## Task:

Produce a “people” file with the following schema. Save it as a CSV with a header line to the working directory.


| Column | Type | Description |
| -------| -----| ------ |
| email | string| Primary email address |
| code | string| Source code |
| code | string| Source code |






is_unsub
boolean
Is the primary email address unsubscribed?
created_dt
datetime
Person creation datetime
updated_dt
datetime
Person updated datetime

