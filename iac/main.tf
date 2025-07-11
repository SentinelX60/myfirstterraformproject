# Terraform configuration block - specifies requirements for this configuration
terraform {
  # Define which providers this configuration requires
  required_providers {
    # Google Cloud Platform provider configuration
    google = {
      source  = "hashicorp/google"  # Official Google provider from HashiCorp registry
      version = "~> 5.0"            # Use version 5.x (allows minor updates, not major)
    }
  }

  # Minimum Terraform version required to run this configuration
  required_version = ">= 1.3.0"
}

# Configure the Google Cloud Provider with authentication and default settings
provider "google" {
  credentials = file(var.credentials_file)  # Path to service account JSON key file
  project     = var.project_id              # GCP project ID where resources will be created
  region      = var.region                  # Default region for regional resources
  zone        = var.zone                    # Default zone for zonal resources
}

# Create a Google Compute Engine virtual machine instance
resource "google_compute_instance" "free_vm" {
  name         = "free-tier-vm"  # Name of the VM instance in GCP console
  machine_type = "f1-micro"      # VM size (f1-micro is eligible for free tier)
  zone         = var.zone        # Availability zone where the VM will be created

  # Configuration for the VM's primary disk
  boot_disk {
    # Settings for initializing the boot disk
    initialize_params {
      image = "debian-cloud/debian-11"  # OS image (Debian 11 from official images)
    }
  }

  # Network configuration for the VM
  network_interface {
    network       = "default"      # Use the default VPC network
    access_config {                # Enable external IP address
      # Empty block means use ephemeral external IP
    }
  }
}
