import os
from azure.identity import ClientSecretCredential
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget
from azureml.core import Experiment
from azureml.core.run import Run

credentials = ClientSecretCredential(
              tenant_id = tenant_id,
              client_id = client_id,
              client_secret = client_secret)

ws = Workspace(
              subscription_id = subscription_id,
              resource_group = resource_group,
              workspace_name = workspace_name,
              auth = credentials)

compute_target = ComputeTarget(worspace = ws, name = 'trial-compute')

run = experiment.submit(
script = 'Users/shudharsananm.1989/my_own_code/github_actions_testing.py', compute_target = compute_target)

if run.status == 'completed':
  print("Run completed")
elif run.status == 'Failed':
  print(f"Run failed with error: {run.error}")
else:
  print(f'Run was {run.status}')
