# Udacity-DevOps-Project3

Clone the repository 

Login to Azure CLI using the az login command
![image](https://user-images.githubusercontent.com/24310615/123080113-81613d00-d414-11eb-8cdf-88edc3a4fc57.png)

Create a resource group to group the resources created in the project, replace <resourcegroup-name> and <location> as required
```sh
az group create --name <resourcegroup-name> --location <location>
```
 Output: 
 ![image](https://user-images.githubusercontent.com/24310615/123095111-9abeb500-d425-11eb-94ea-1dcc7848a4ec.png)

 
Create a storage account using the below command, <resourcegroup-name> is same as previous step and a unique name for <storage-account>
```sh
az storage account create --resource-group <resourcegroup-name> --name <storage-account> --sku Standard_LRS
```

 Output:
 ![image](https://user-images.githubusercontent.com/24310615/123095281-d48fbb80-d425-11eb-93ab-31cea65914ea.png)

 
 Get the account key of the storage account created earlier
```sh
az storage account keys list -g <resource-group> -n <storage-account>
```
 Output :
 ![image](https://user-images.githubusercontent.com/24310615/123095628-2cc6bd80-d426-11eb-9130-3c2a75bb0e23.png)

 
Copy the value of they key and create Blob contianer to store the Terraform state
```sh
az storage container create --name <container-name> --account-name <storage-account> --account-key <account-key>
```
Output : 
 ![image](https://user-images.githubusercontent.com/24310615/123095899-73b4b300-d426-11eb-97cf-bdd71d5649d0.png)

 
 Update the Storage details(storage account name, container name and access_key) in terraform main.tf file
 ```sh
  backend "azurerm" {
    storage_account_name = ""
    container_name       = ""
    key                  = "terrafom.tfstate"
    access_key           = ""
  }
 ```
 
