//Using Terraform to provision the infrastructure in my linode workspace

terraform {
    required_providers {
        linode = {
            source = "linode/linode"
      }
    }
}

provider "linode" {
    token = "API-TOKEN"
}

resource "linode_instance" "vm" {
    label = var.label
    image = var.image
    type = var.type
    root_pass = "PASS"
    region = "REGION"
}

output "ipv4_address" {
    value = linode_instance.vm.ip_address
}
