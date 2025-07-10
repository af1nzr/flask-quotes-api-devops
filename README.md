# 🚀 Flask Quotes API – Dockerized & Kubernetes Deployment

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

A production-ready Flask REST API serving inspirational quotes, containerized with Docker and deployed on Kubernetes via Minikube. Complete with CI/CD pipeline using GitHub Actions.

## 🌟 Features

- **RESTful API** built with Flask (Python)
- **Containerized** with Docker for consistent environments
- **Kubernetes deployment** with Minikube for local development
- **CI/CD pipeline** via GitHub Actions
- **GitHub Container Registry (GHCR)** for Docker image storage
- **Scalable architecture** with 3 replicas in Kubernetes
- **Health checks** and readiness probes (optional)
- **Production-grade** configuration

## 📦 Project Structure

<pre>
  flask-quotes-api/
├── app/ # Flask application source code
│ ├── init.py # Flask app initialization
│ ├── routes.py # API endpoints
│ └── quotes.py # Quotes data/logic
├── k8/ # Kubernetes manifests
│ ├── deployment.yml # K8s Deployment configuration
│ └── service.yml # K8s Service configuration
├── tests/ # Unit and integration tests
├── .github/workflows/ # CI/CD workflows
│ └── ci.yml # GitHub Actions pipeline
├── Dockerfile # Docker build instructions
├── requirements.txt # Python dependencies
├── run.py # Application entry point
└── README.md # You are here
</pre>


## 🚀 Quick Start

### Prerequisites
- Docker
- Minikube
- kubectl
- Python 3.8+

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/flask-quotes-api.git
cd flask-quotes-api

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask development server
flask run
```
## Docker Build & Run
```
# Build the Docker image
docker build -t flask-quotes-api .

# Run the container
docker run -p 5000:5000 flask-quotes-api
```

## Kubernetes Deployment with Minikube
```
# Start Minikube cluster
minikube start

# Enable Minikube's Docker daemon
eval $(minikube docker-env)

# Build image in Minikube's Docker environment
docker build -t flask-quotes-api .

# Apply Kubernetes manifests
kubectl apply -f k8/deployment.yml
kubectl apply -f k8/service.yml

# Check deployment status
kubectl get pods -w

# Access the service
minikube service flask-quotes-api-service
```

### 🔄 CI/CD Pipeline

The GitHub Actions workflow (ci.yml) automatically:
- Builds the Docker image on push to main
- Pushes the image to GitHub Container Registry (GHCR)
- (Optional) Deploys to Kubernetes cluster

### 📚 API Endpoints
Endpoint	Method	Description
/	GET	Welcome message
/quotes	GET	Retrieve all quotes
/quotes/random	GET	Get a random quote
/health	GET	Health check endpoint

Example request:
```
curl http://localhost:5000/quotes
```

🔍 Monitoring
```
# View pod logs
kubectl logs -f <pod-name>

# Check deployment status
kubectl get deployments

# View service details
kubectl describe service flask-quotes-api-service

# Port forwarding for local access
kubectl port-forward svc/flask-quotes-api-service 5000:5000
```
### 🛡️ Security Considerations
For production, ensure to:

Use HTTPS with proper TLS certificates
Implement authentication/authorization
Secure Kubernetes secrets for sensitive data
Set resource limits in deployment

### 🤝 Contributing

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

### 📜 License
Distributed under the MIT License. See LICENSE for more information.





