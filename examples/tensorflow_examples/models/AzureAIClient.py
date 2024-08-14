from azure.ai.resources.client import AIClient
from azure.identity import DefaultAzureCredential

ai_client = AIClient(credential=DefaultAzureCredential(), subscription_id='subscription_id',
                     resource_group_name='resource_group', project_name='project_name')
