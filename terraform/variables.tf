variable "credentionals" {
  description = "My credentionals"
  default     = "../keys/gcp_credentials.json"
}

variable "region" {
  description = "Region"
  default     = "europe-west1"
}

variable "project" {
  description = "GCP Project"
  default     = "us-accidents-421114"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "gcp_bucket_name" {
  description = "Storage Bucket Name"
  default     = "us-accidents-bucket"
}

variable "gcs_strorage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}