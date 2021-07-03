### Udacity-DevOps-Project3

# Project Overview

In this project we will build a disposable test environment and ensure the quality of the application with various automated testing (Regression,Functional UI and Performance) and also  monitor and provide insight into the application's behavior, and determine root causes by querying the application’s custom log file.

![image](https://user-images.githubusercontent.com/24310615/124194544-af074f80-dac0-11eb-86ab-5d1171347c61.png)

# Tools Used 

Azure DevOps
Selenium
Terraform
JMeter
Postman
Azure Monitor
Azure Log Analytics

# Getting Started

# Setting up the terraform backend

1.Create a SSH key using the below command , upload the generated public key in github and clone the repository 
  ```sh
  ssh-keygen -t rsa
  ```

2.Login to Azure CLI using the az login command

3.Create a resource group to group the resources created in the project, replace <resourcegroup-name> and <location> as required
This resource group will hold the storage account used as terraform backend
 
```sh
az group create --name <resourcegroup-name> --location <location>
```

4.Create a storage account using the below command, <resourcegroup-name> is same as previous step and a unique name for <storage-account>
 
```sh
az storage account create --resource-group <resourcegroup-name> --name <storage-account> --sku Standard_LRS
``` 
 5. Get the account key of the storage account created earlier. This key will be used to create container in the storage account

```sh
az storage account keys list -g <resource-group> -n <storage-account>
```
 
6.Copy the value of they key and create Blob contianer to store the Terraform state. 
```sh
az storage container create --name <container-name> --account-name <storage-account> --account-key <account-key>
```

 
7.Update the Storage details(storage account name, container name and access_key) in terraform main.tf file

 ```sh
  backend "azurerm" {
    storage_account_name = ""
    container_name       = ""
    key                  = "terrafom.tfstate"
    access_key           = ""
  }
 ```
 
8.Create a Service principle to grant access to Azure Resources
```sh
 az ad sp create-for-rbac --name="Terraform" --role="Contributor" 
```
 
9. Note down the appid, password and tenant id and update the terraform.tfvars file
```sh
subscription_id = ""
client_id = ""
client_secret = ""
tenant_id = ""
 ```
 
 10. Create a Log analytics workspace and copy the agent registration script. This script will be later executed once the VM is created
 
 11. Create a custom log in the log analytics workspace. Upload the selenium-sample.log , delimited by timestamp and provide the linux vm path as \selenium\log
 
 
 12. Create a project in Azure DevOps if not already created
 
 13. Install the below Extensions :

      a.JMeter (https://marketplace.visualstudio.com/items?itemName=AlexandreGattiker.jmeter-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList)

      b.Terraform (https://marketplace.visualstudio.com/items?itemName=ms-devlabs.custom-terraform-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList)

 
 14. Create a service connection of type Azure Resource Manager (name the service as azrm-sc)
 
 15. Create an Environment with name TEST
 
 16. Add a Virtual Machine resource to the environment and copy the registration script. This script will be later executed in the virtual machine created in the terraform which      will allow pipeline to run ssh commands on the VM.
 
 
 17. Upload the terraform.tfvars file and the public key (id_rsa.pub) in the secure library
 
 18. Create a new pipeline , select the repository and select Github and build pipeline from existing yaml file
 
 19. Modify the yaml file with the Service connection name, Environment names
 
 20. Add a pipeline variable "SSH-Public-Key" and copy the value of Public Key created earlier
 
 21. Once the infrastructure is povisioned, ssh into the created VM and execute the scripts copied from steps 10 and 16
 
 22. After the pipeline is executed successfully the below artifactes wiill be available in the pipeline
 
 
 23. In Azure portal create a alert on the App Service that is created from the pipeline
     
 24. After the alert rule is successfully created, try to alert some alert by navigating to invalid URL. 
 
 25. Once the threshold limit has exceeded, an email will sent to the specified email address.
 
