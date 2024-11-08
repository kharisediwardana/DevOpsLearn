This is simple python project with purpose to make a deployment process

HOW TO RUN with Docker

# Build Docker

docker build -t my-python-app .

# Run Docker

docker run -d -p 5003:5003 my-python-app (following port on code and available)

# Run Terraform

Terraform init
Terraform Apply

# can start from this step

gcloud auth login
gcloud compute ssh --zone=us-central1-a terraform-instance

# Start Nginx

sudo systemctl start nginx
sudo systemctl enable nginx
