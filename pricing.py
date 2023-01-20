import requests
import os
import json

url = "https://cloudbilling.googleapis.com/v1/services"

try: 
    os.mkdir('./GCP_DATA') 
except:
    pass 


def save_data(json_data, service_name):
    filename = './GCP_DATA/{}.json'.format(service_name)
    if os.path.exists(filename):
        with open(filename, 'r+') as json_file:
            # file exists
            # load the existing data
            json_file_data = json.load(json_file)
            # join new data with existing
            print('adding new data')
            for data in json_data['skus']:
                json_file_data['skus'].append(data)

            json_file_data['nextPageToken']=json_data['nextPageToken']
            # set file position to offset
            json_file.seek(0)
            # convert back to json
            json.dump(json_file_data, json_file, indent=4)

    else:
        with open(filename, 'a') as json_file:
            print('creating file and adding new data')
            json.dump(json_data, json_file, indent=4)

def get_service_data(API_KEY,SERVICE_ID,service,nextPageToken=''):
    
    if nextPageToken != '':
        service_url = url+"/" + SERVICE_ID + "/skus?pageToken=" + nextPageToken + "&key=" + API_KEY
    else:
        service_url = url+"/" + SERVICE_ID + "/skus?key=" + API_KEY 

    json_data = requests.get(service_url).json()

    save_data(json_data, service)

    if json_data["nextPageToken"] != '':
        get_service_data(API_KEY,SERVICE_ID,service,json_data["nextPageToken"])


def get_data(url,nextPageToken=''):

    SERVICE_ID = ""
    API_KEY = 'AIzaSyD39kaXRm3BTfW8rOCS-IYaVcNFivOfiN0'#os.environ["API_KEY"]
    services_required = ["Compute Engine", "App Engine",
                         "Kubernetes Engine", "Cloud Storage", "Cloud SQL", "Cloud Tasks"]

    service_data = get_services_index(url, API_KEY)
    services = service_data["services"]

    for service in services:
        service_selected = service["displayName"]
        if service_selected in services_required:
            SERVICE_ID = service["serviceId"] 
            get_service_data(count,API_KEY,SERVICE_ID,service_selected) 

def get_services_index(url, API_KEY):
    url = url + "?key=" + API_KEY
    json_data = requests.get(url).json()

    with open('gcp_services.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    return json_data


get_data(url)