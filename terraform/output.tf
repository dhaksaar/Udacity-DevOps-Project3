output "publicip" {
  description = "Public ip of the VM"
  value       = module..publicip.*.ip_address
}

