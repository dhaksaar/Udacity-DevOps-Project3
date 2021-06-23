# Udacity-DevOps-Project3

Clone the repository 

Login to Azure CLI using the az login command
![image](https://user-images.githubusercontent.com/24310615/123079323-bf119600-d413-11eb-820a-52de89befb85.png)

Create a resource group to group the resources created in the project, replace <resourcegroup-name> and <location> as required
```sh
az group create --name <resourcegroup-name> --location <location>
```
Create a storage account using the below command, <resourcegroup-name> is same as previous step and a unique name for <storage-account>
```sh
az storage account create --resource-group <resourcegroup-name> --name <storage-account> --sku Standard_LRS
```
 Get the account key of the storage account created earlier
```sh
az storage account keys list -g <resource-group> -n <storage-account>
```
Create Blob contianer to store the Terraform state
```sh
az storage container create --name <container-name> --account-name <storage-account> --account-key <account-key>
```
