resource "google_compute_instance" "vm_instance" {
	project = var.project_id
	name = var.machine_name
	machine_type = var.machine_type
	zone = var.zone
	boot_disk {
		initialize_params {
			image = "centos-stream-9"
		}
		}

	network_interface {
		network = var.network
		subnetwork = var.subnetwork
		access_config {
		}	
	}
	
	tags = ["ssh", "devops-course"]
	
}
