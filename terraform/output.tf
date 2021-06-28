output "publicip" {
  description = "Public ip of the VM"
  value       = module.publicip.public_ip_address
}

