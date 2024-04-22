terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentionals)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "us-accidents-bucket" {
  name          = var.gcp_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "us_accidents_raw"
  friendly_name               = "US accidents Raw"
  description                 = "US accidents Raw Dataset"
  location                    = var.location
  default_table_expiration_ms = 2592000000

  labels = {
    env = "default"
  }
}

resource "google_bigquery_dataset" "analytics-dataset" {
  dataset_id                  = "us_accidents_analytics"
  friendly_name               = "US accidents Analytics"
  description                 = "US accidents Analytics Dataset"
  location                    = var.location
  default_table_expiration_ms = 2592000000

  labels = {
    env = "default"
  }
}