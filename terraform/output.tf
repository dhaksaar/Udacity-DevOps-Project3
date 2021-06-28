output "publicip" {
  description = "Public ip of the VM"
  value       = module.vm.public_ip_address_id.ip_address
}

