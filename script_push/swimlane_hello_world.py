import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


url = os.getenv("http://soar-prod.bluebastion.local/api")
api_key = os.getenv("api_key")

{
  "application": {
    "description": "string",
    "acronym": "string",
    "trackingFieldId": "string",
    "layout": [
      {
        "id": "string",
        "parentId": "string",
        "row": 0,
        "col": 0,
        "sizex": 0,
        "sizey": 0,
        "layoutType": "None"
      }
    ],
    "fields": [
      {
        "id": "string",
        "name": "string",
        "key": "string",
        "sourceAppletFieldId": "string",
        "sourceAppletId": "string",
        "fieldType": "None",
        "required": True,
        "readOnly": True,
        "supportsMultipleOutputMappings": True
      }
    ],
    "maxTrackingId": 0,
    "workspaces": [
      "string"
    ],
    "createWorkspace": True,
    "createdDate": "string",
    "createdByUser": {
      "id": "string",
      "name": "string"
    },
    "modifiedDate": "string",
    "modifiedByUser": {
      "id": "string",
      "name": "string"
    },
    "timeSpentFieldId": "string",
    "timeTrackingEnabled": True,
    "permissions": {
      "additionalProp1": {
        "type": "string",
        "id": "string",
        "name": "string",
        "access": "None",
        "fields": {
          "additionalProp1": "None",
          "additionalProp2": "None",
          "additionalProp3": "None"
        }
      },
      "additionalProp2": {
        "type": "string",
        "id": "string",
        "name": "string",
        "access": "None",
        "fields": {
          "additionalProp1": "None",
          "additionalProp2": "None",
          "additionalProp3": "None"
        }
      },
      "additionalProp3": {
        "type": "string",
        "id": "string",
        "name": "string",
        "access": "None",
        "fields": {
          "additionalProp1": "None",
          "additionalProp2": "None",
          "additionalProp3": "None"
        }
      }
    },
    "uid": "string",
    "version": 0,
    "id": "string",
    "name": "string",
    "disabled": True
  },
  "errors": [
    "string"
  ]
}

script_data = {
    "name": "Hello World",
    "description": "This script prints Hello, world!",
    "code": "print('Hello, world!')"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send a POST request to create the new script
response = requests.post(url="http://soar-prod.bluebastion.local/api", headers=headers, json=script_data, verify=False)

# Check the status code of the response
if response.status_code == 200:
    print("Script created successfully!")
else:
    print("Error creating script: " + response.text)



