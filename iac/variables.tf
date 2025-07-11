# Variable definition for the GCP project ID
variable "project_id" {
  description = "Your GCP project ID"  # Human-readable description of this variable
  type        = string                 # Data type constraint (must be a string)
}

# Variable definition for the GCP region
variable "region" {
  description = "GCP region"       # Description of what this variable represents
  type        = string             # Data type constraint (must be a string)
  default     = "us-central1"      # Default value if not specified in terraform.tfvars
}

# Variable definition for the GCP availability zone
variable "zone" {
  description = "GCP zone"         # Description of what this variable represents
  type        = string             # Data type constraint (must be a string)
  default     = "us-central1-a"    # Default value if not specified in terraform.tfvars
}

# Variable definition for the service account credentials file path
variable "credentials_file" {
  description = "Path to the service account credentials JSON file"  # Description
  type        = string                                               # Data type constraint
}
