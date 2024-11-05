# Vertex AI set up instructions

## Set up a project and a development environment

https://cloud.google.com/vertex-ai/docs/start/cloud-environment

## Install the Vertex AI SDK for Python

https://cloud.google.com/vertex-ai/docs/start/install-sdk

Note: the instructions on the install-sdk link have the following steps:

Installation of the Vertex AI SDK for Python includes the following steps:
1. Create an isolated Python environment
2. Install the Vertex AI SDK package
3. Initialize the Vertex AI SDK (This is done within the python script itself)

However, step 3 is done from within the python script itself.

## Install Python dependencies in requirements.txt file after activating your Python virtual environment
1. Create an isolated Python environemnt and activate it (https://cloud.google.com/python/docs/setup#linux)
2. Run the following command to install Python dependencies in the requirements.txt file:
```
python -m pip install -r requirements.txt
```

## Environment variables in .env file
PROJECT_ID: Your Google Cloud Provider project id.

## For Windows VSCode (WSL required https://learn.microsoft.com/en-us/windows/wsl/install)
1. Open a WSL terminal
2. Run the following command to open the folder within a WSL window.
```
code .
```

## Script execution:
```
python vertex_ai_demo.py
```

## More code samples for image generation

https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-imagen-generate-image

## Request to increase Vertex AI quota
1. Navigate to https://console.cloud.google.com/iam-admin/quotas
2. Click on Edit Quota for the desired service.
![Edit Quote Button](instructions_images/edit_quota.PNG)
3. Fill out the form for the request.
![Quota Changes Form](instructions_images/quota_changes_form.PNG)