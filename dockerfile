# CodeSandbox supports debian & ubuntu based images
FROM ubuntu:latest
 
# Set the working directory to /workspace
WORKDIR /workspace


RUN apt update && \
    apt upgrade -y && \
    apt install -y python3-pip python3-venv
    
  # Create a virtual environment
RUN python3 -m venv /workspace/venv
# Activate the virtual environment
ENV PATH="/workspace/venv/bin:$PATH"

# Install virtualenv and packages from requirements.txt
COPY requirements.txt /workspace
COPY dags /workspace/airflow/dags

RUN pip install -r requirements.txt


# Expose port 8080
EXPOSE 8080
# Verify the installation and start Airflow
CMD ["bash", "-c","export AIRFLOW_HOME=/workspace/airflow && airflow version && airflow standalone"]


