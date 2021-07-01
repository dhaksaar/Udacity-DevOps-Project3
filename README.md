### Udacity-DevOps-Project3

#Project Overview

In this project we will build a disposable test environment and ensure the quality of the application with various automated testing (Regression,Functional UI and Performance) and also  monitor and provide insight into the application's behavior, and determine root causes by querying the application’s custom log file.

![image](https://user-images.githubusercontent.com/24310615/124194544-af074f80-dac0-11eb-86ab-5d1171347c61.png)

#Tools Used 

Azure DevOps
Selenium
Terraform
JMeter
Postman
Azure Monitor
Azure Log Analytics

#Getting Started

#Setting up the terraform backend

1.Create a SSH key and clone the repository 

2.Login to Azure CLI using the az login command

![image](https://user-images.githubusercontent.com/24310615/123080113-81613d00-d414-11eb-8cdf-88edc3a4fc57.png)


3.Create a resource group to group the resources created in the project, replace <resourcegroup-name> and <location> as required
This resource group will hold the storage account used as terraform backend
 
```sh
az group create --name <resourcegroup-name> --location <location>
```

Output: 
 ![image](https://user-images.githubusercontent.com/24310615/123095111-9abeb500-d425-11eb-94ea-1dcc7848a4ec.png)

4.Create a storage account using the below command, <resourcegroup-name> is same as previous step and a unique name for <storage-account>
 
```sh
az storage account create --resource-group <resourcegroup-name> --name <storage-account> --sku Standard_LRS
```

 Output:
 ![image](https://user-images.githubusercontent.com/24310615/123095281-d48fbb80-d425-11eb-93ab-31cea65914ea.png)

 
 5. Get the account key of the storage account created earlier. This key will be used to create container in the storage account
```sh
az storage account keys list -g <resource-group> -n <storage-account>
```
 Output :
 ![image](https://user-images.githubusercontent.com/24310615/123095628-2cc6bd80-d426-11eb-9130-3c2a75bb0e23.png)

 
6.Copy the value of they key and create Blob contianer to store the Terraform state. 
```sh
az storage container create --name <container-name> --account-name <storage-account> --account-key <account-key>
```
Output : 
 ![image](https://user-images.githubusercontent.com/24310615/123095899-73b4b300-d426-11eb-97cf-bdd71d5649d0.png)

 
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
 Output 
 ![image](https://user-images.githubusercontent.com/24310615/123100366-f7709e80-d42a-11eb-90c5-4c0bf8ee40f7.png)

9. Note down the appid, password and tenant id and update the terraform.tfvars file
```sh
subscription_id = ""
client_id = ""
client_secret = ""
tenant_id = ""
 ```
 10. Create a project in Azure DevOps if not already created
 
 11. Install these Extensions :
 
 a.JMeter (https://marketplace.visualstudio.com/items?itemName=AlexandreGattiker.jmeter-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList)

 b.Terraform (https://marketplace.visualstudio.com/items?itemName=ms-devlabs.custom-terraform-tasks&targetId=625be685-7d04-4b91-8e92-0a3f91f6c3ac&utm_source=vstsproduct&utm_medium=ExtHubManageList)
 
 
 12. Create a service connection of type Azure Resource Manager (name the service as azrm-sc)
 
 13. Create an Environment with name TEST
 
 14.Upload the terraform.tfvars file and the private key in the secure library
 
 15. Create a new pipeline , select the repository and select Github and build pipeline from existing yaml file
 
 16. Modify the yaml file with the Service connection name
 
 
 
 
 
