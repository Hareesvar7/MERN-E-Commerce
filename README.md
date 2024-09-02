# MERN-E-Commerce

Check it out!!!
https://mern-0fo7.onrender.com/

In this project we can access it with two ways as an seller and consumer.

# Run frontend (:3000) & backend (:5000)
npm run dev

# Import data
npm run data:import

# Sample User Logins

admin@email.com (Admin)

Password = 123456

dummy@gmail.com

Password = 12345

# Web Server

1. https://mern-0fo7.onrender.com/cart   = For cart navigation.
2. https://mern-0fo7.onrender.com/login  = For login  navigation.
3. https://mern-0fo7.onrender.com/register  = For register  navigation.
4. https://mern-0fo7.onrender.com/productname  = For product  navigation.


from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace with your Azure subscription ID
subscription_id = 'your_subscription_id'

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

# Define tag key and value
tag_key = 'your_tag_key'
tag_value = 'your_tag_value'

# List resources with the specified tag
def list_resources_by_tag(tag_key, tag_value):
    resources = resource_client.resources.list(
        filter=f"tagName eq '{tag_key}' and tagValue eq '{tag_value}'"
    )
    return resources

# Delete resources with the specified tag
def delete_resources_by_tag(tag_key, tag_value):
    resources = list_resources_by_tag(tag_key, tag_value)
    for resource in resources:
        print(f"Deleting resource: {resource.id}")
        resource_client.resources.delete_by_id(resource.id, api_version='2021-04-01')

if __name__ == "__main__":
    delete_resources_by_tag(tag_key, tag_value)
