# FastAPI Key-Value Store

This project implements a simple key-value store using FastAPI, Redis, and Huey. It provides endpoints to get, set, and delete key-value pairs, with asynchronous task execution using Huey. This project also includes the Kubernetes file for implementing persistent volume , deployment, service and autosacling also.

## Setup

### Local Development (without Docker)

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Install and Run Redis on port "6379". See the [Redis Installation documentation](https://redis.io/docs/install/install-redis/ "Redis website") for more details.

3. Start the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

4. Run the Huey worker in a separate terminal:

    ```bash
    huey_consumer.py tasks.huey
    ```

### Local Development (with Docker)

1. Install and run Docker on your System. See the [Docker Installation documentation](https://docs.docker.com/engine/install/ "Docker website") for more details.

2. Build docker image for the app

    ```bash
    docker build -t key_value .
    ```

3. Start the FastAPI app on Docker container:

    ```bash
    docker run -p 8000:8000 key_value
    ```

    Your app is now running on :- http://localhost:8000/


### Kubernetes Deployment

1. Install and run Docker on your Server. See the [Docker Installation documentation](https://docs.docker.com/engine/install/ "Docker website") for more details.

2. Install Kubernetes on your Server. See the [Kubernetes Installation documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/ "Kubernetes website") for more details.

3. Apply Kubernetes manifests:

    ```bash
    kubectl apply -f k8s/
    ```
    And your app is now deployed. You can access the application at http://<your-server-public-ip>:31787, but make sure you have allowed incoming TCP connections to port 31787 on your server or hosting environment.


### Autoscaling (Horizontal Pod Autoscaler)

The Kubernetes deployment includes Horizontal Pod Autoscaler (HPA) for automatic scaling based on CPU utilization.

Ensure your Kubernetes cluster supports Horizontal Pod Autoscaler.

To manually test autoscaling, you can use a tool like `hey`:

```bash
hey -z 30s -c 10 http://localhost:8000/get/sample_key
```

This command simulates traffic and may trigger autoscaling based on the HPA configuration.

### Cleanup

To clean up the Kubernetes resources:
```bash
kubectl delete -f k8s/
```


### Notes

Ensure you have a running Redis server accessible to the FastAPI app and the Huey worker. Adjust the Redis configuration in main.py and huey_worker.py accordingly.
Customize the Kubernetes manifests (k8s/) based on your specific environment and requirements.


### Link

I also deployed the application on a server. I dont know how long i will keep it running but you can access it on : http://20.197.47.122:31787/
