# Interviewer Notes

This repository demonstrates a minimal Terraform deployment of a Google Compute Engine free-tier VM. The repository has been sanitized for public review.

Quick summary:
- Deploys one `f1-micro` Debian 11 VM in `us-central1-a`.
- Provider: Google Cloud (`hashicorp/google` 5.x).
- Variables are declared in `iac/variables.tf`; example variable values are in `iac/terraform.tfvars.example`.

Security and setup notes:
- No service-account JSON keys or real credentials are tracked in this repo.
- The following patterns and files are ignored via `.gitignore`: `*.json`, `terraform.tfvars`, `.terraform/`.
- If you want to run this locally, create your own `iac/terraform.tfvars` with a path to a local service account key and ensure that key is never committed.

Commands to test locally:
```bash
cd iac
terraform init
terraform plan
terraform apply
```

Note: When running `terraform apply`, the service account key file must be available locally and specified via `credentials_file` in your local `terraform.tfvars`.

Contact: SentinelX60
