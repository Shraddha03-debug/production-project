# Production-Style DevOps Deployment Project

A Django app taken through the full DevOps lifecycle — containerized
with Docker, deployed on Kubernetes, infrastructure defined with
Terraform, and built/tested/deployed through a GitHub Actions
pipeline.

## Flow

Application -> Git -> Docker -> Container Registry -> Terraform ->
Cloud Infrastructure (AWS) -> Kubernetes -> CI/CD -> Monitoring

## Project Structure

- app/ — Django application + Dockerfile
- k8s/ — Kubernetes manifests
- terraform/ — AWS infrastructure (VPC + EKS) as code
- .github/workflows/ — CI/CD pipeline
- SECURITY_AND_OPERATIONS.md — secrets, rollback, monitoring notes

## Running it locally

Go to the app folder and run:

    cd app
    docker compose up

App: http://localhost:8000
Admin panel: http://localhost:8000/admin
Health check: http://localhost:8000/healthz

## Deploying to Kubernetes (local cluster)

    kubectl apply -f k8s/namespace.yaml
    kubectl apply -f k8s/secret.yaml
    kubectl apply -f k8s/configmap.yaml
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    kubectl -n devops-demo get pods

Note: copy k8s/secret.yaml.example to k8s/secret.yaml and fill in a
real base64-encoded value before applying.

## Infrastructure (Terraform)

    cd terraform
    terraform init
    terraform validate
    terraform plan

terraform apply provisions a VPC (public + private subnets across 2
AZs) and an EKS cluster with a managed node group. Not applied by
default — requires AWS credentials.

## CI/CD

On every push to main, GitHub Actions:

1. Runs the Django test suite
2. Builds the Docker image
3. Scans it for vulnerabilities (Trivy)
4. Pushes it to GitHub Container Registry
5. Deploy step is currently disabled, to be enabled once a live
   cluster exists


