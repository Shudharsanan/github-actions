import os
from azure.identity import ClientSecretCredential
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget
from azureml.core import Experiment
from azureml.core.run import Run
from azure.storage.blob import BlobServiceClient


tenant_id = "ee10b4ad-568d-4026-9cca-3f47d86d0d04"
client_id = "c8533615-50a1-4b7b-87a3-0e1655b2c357"
client_secret = "QxC8Q~b_m1EYYfKMuSkRRjhzp-5L9ZlEJTjhZdsc"
subscription_id = "89932198-e74d-4f28-b227-95f2729192c0"
resource_group = "rg-dp100-labs"
workspace_name = "mlw-dp100-labs"

credentials = ClientSecretCredential(
              tenant_id = tenant_id,
              client_id = client_id,
              client_secret = client_secret)

blob_service_client = BlobServiceClient(account_url="https://mlwdp100labs7488979237.blob.core.windows.net", credential=credentials)

containers = blob_service_client.list_containers()
for container in containers:
    print(container.name)

ws = Workspace(
              subscription_id = subscription_id,
              resource_group = resource_group,
              workspace_name = workspace_name)
#              auth = credentials)

compute_target = ComputeTarget(workspace = ws, name = 'trial-compute')



#run = experiment.submit(script = 'Users/shudharsananm.1989/my_own_code/github_actions_testing.py', compute_target = compute_target)

#if run.status == 'completed':
#  print("Run completed")
#elif run.status == 'Failed':
#  print(f"Run failed with error: {run.error}")
#else:
#  print(f'Run was {run.status}')
