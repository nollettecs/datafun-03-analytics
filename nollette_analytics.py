# Module 3

"""Module 3: Goal to fetch data from a 
URL, process it with Python, individualize the data, and push it to Github"""

# Standard library imports
import csv
import pathlib
from pathlib import Path
import json
import pandas as pd
import io
from io import StringIO


# External library imports
import requests

# Local module imports (still can't get my previous projects to import)

#creating a class since previous projects wont import

class YourNameAttr:
    def __init__(self, name):
        self.my_name_string = name

yourname_attr = YourNameAttr("Cole Nollette")





""" Function 1: Fetching a text file"""
# Creating function to fetch web data
# Function 1 Process Text Data
# Attempted to use Dr. Case's Shakespeare file but didnt work. Switched to what others were using.
def fetch_and_write_txt_data (folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file (folder_name, filename, response.text)
    else:
        print(f"Failed to fetch text data: {response.status_code}")

# Function to write file
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w', encoding='utf-8') as file:
        file.write(data)
        print(f"Text data save to {file_path}")

# Process the write Data
def process_txt_file(folder_name, input_filename, output_filename):
    txt_url = 'https://www.gutenberg.org/cache/epub/72796/pg72796.txt.utf-8'
    response = requests.get(txt_url)

    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        processed_data = data
        write_txt_file(folder_name, output_filename, processed_data)
    else:
        print(f"failed to fetch data: {response.status_code}")





"""Function 2: Fetching a CSV file"""

# Function 2 Process CSV Data
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")


# Function to write file        
def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    csv_data = parse_csv_data(data)

    with file_path.open('w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)
        print(f"CSV data saved to {file_path}")

# Function to parse CSV data
def parse_csv_data(csv_text):
    csv_data = []
    csv_reader = csv.reader(StringIO(csv_text))
    for row in csv_reader:
        csv_data.append(row)
    return csv_data

# Function to process CSV data
def process_csv_file(csv_folder_name, input_filename, output_filename):
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    response = requests.get(csv_url)

    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)
        processed_data = data
        write_csv_file(csv_folder_name, output_filename, processed_data)

    else:
        print(f"Failed to fetch data: {response.status_code}")






"""Function 3: Fetching an Excel File"""

# Function 3 Process Excel Data
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


# Function to write file
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)
    
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(data)
        print (f"Excel data saved to file {file_path}")


# Function to process Excel data
def process_excel_file(excel_folder_name, input_filename, output_filename):
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    response = requests.get(excel_url)

    if response.status_code == 200:
        data = response.content
        write_excel_file(excel_folder_name, input_filename, data)

        excel_data = pd.read_excel(io.BytesIO(data))
        processed_data = excel_data.to_csv(index=False)
        csv_output_filename = output_filename.replace ('.xls', '.csv')
        write_csv_file(excel_folder_name, csv_output_filename, processed_data)

    else:
        print(f"Failed to fetch data: {response.status_code}")





"""Function 4: Fetching a JSON file"""

#Function 4 Process JSON Data
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data: {response.status_code}")


# Function to write file
def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('wb') as file:
        file.write(data)
        print(f"Binary data save to {file_path}")


# Function to process data
def process_json_file(json_folder_name, input_filename, output_filename):
    json_url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(json_url)

    if response.status_code == 200:
        data = response.content
        write_json_file(json_folder_name, input_filename, data)
        write_json_file(json_folder_name, output_filename, data)

    else:
        print(f"Failed to fetch data: {response.status_code}")

# Implementing Exception Handling
        
import requests
from pathlib import Path

def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def main():
    """ Main function to demonstrate module capabilities"""

    print (f"Name: {yourname_attr.my_name_string}")

    txt_url = 'https://www.gutenberg.org/cache/epub/72796/pg72796.txt.utf-8'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'

    json_url = 'http://api.open-notify.org/iss-now.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

if __name__ == "__main__":
    main()