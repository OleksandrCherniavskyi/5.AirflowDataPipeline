# 5.AirflowDataPipeline

AirflowDataPipeline is a data collection project designed to automate the process of extracting data from a website and storing it in a SQL database using Airflow.In summary, AirflowDataPipeline provides a powerful and efficient way to collect and store data from a website in a SQLite database using Airflow, offering a scalable and reliable solution for data collection and management.

## Installation

 ### 1. If you have Docker Desktop

- download repository
- open terminal in your favorit IDE or command line
- in terminal: 
- cd docker_demo
- docker build -t image_name .
- docker run -p 8080:8080 image_name
- in your favorite browser open http://localhost:8080

![obraz](https://user-images.githubusercontent.com/105165580/231084365-b277fb66-3795-4857-b307-d4cc3fa33ab4.png)
> Where **login** : **admin**, password you can find in container file sestem  docker desktop **standalone_admin_password.txt**
- Run dag_1 > Trigger DAG


### 2. Another way
Open linux command line
- mkdir workspace
- apt update
- apt upgrade
- apt install python3-pip
- apt install python3-venv
- python3 -m venv  /workspace/venv
- source  /workspace/bin/activate
- pip install virtualenv
- pip install pandas
- pip install apache-airflow
- export AIRFLOW_HOME=/workspace/airflow
- airflow version
- add dags in /workspace/airflow/dags
- airflow standalone
- in your favorite browser open http://localhost:8080
- 
![obraz](https://user-images.githubusercontent.com/105165580/231084365-b277fb66-3795-4857-b307-d4cc3fa33ab4.png)
> Where **login** : **admin** **/workspace/airflowstandalone_admin_password.txt** or in **command line**
- Run dag_1 > Trigger DAG

