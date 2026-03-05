# Docker Notes

    - Docker Image: complete snapshot of the entire operating system -> daemon creates a container based on the image
        - container is stateless, doesn't preserve state (when we exit container and rerun using image, back to the default image)

    ex command of docker run:
        > docker run -it python:3.13.11
        > docker run -it --entrypoint=bash python:3.13.11-slim

    > docker ps: show running containers
    > docker ps -a : show all containers

    > docker rm `docker ps -aq`  # delete all containers (list of ids)

    To run a script (like script.py), use volumes
        - the folder test/ should be on the machine as well as in the container

        to get working directory of a folder: echo $(pwd)/test

        > docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3
.13.11-slim
            -v host_path:container_path
                this command mounts a directory from your machine into the container 


Physical Machine - Mac
    ↓
Virtual Machine (VM) - Codespaces
    ↓
Container - Docker
    ↓
Python Virtual Environment - venv/uv inside if needed

example workflow

AWS EC2 VM
    └── Docker
            └── Airflow container
                    └── Python environment
                            └── ETL pipeline


    python -m : run module