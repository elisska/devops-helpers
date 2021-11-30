provider "google" {
  region  = var.region
  zone    = var.zone
  project = var.project_id
  #credentials = file("/downloads/compute-instance.json")
}
