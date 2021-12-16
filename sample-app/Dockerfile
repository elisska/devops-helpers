FROM python:3.7-slim

# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
# this will create /app directory in Docker image
WORKDIR /app

# add group and user to run a container
RUN groupadd -r webservice && useradd --no-log-init -r -g webservice webservice

# this will install some packages
RUN pip install networkx dash plotly

# this will copy application code to working directory
#COPY . /app/
COPY . .

USER webservice:webservice

# indicates the ports on which a container listens for connections
EXPOSE 8050

# this command is started when container is ran
# this is a form with PID 1 issues
#CMD python GraphAnalysis.py obj_dependency_data.csv

# this command is started when container is ran
# below is recommended form of CMD
CMD ["python", "GraphAnalysis.py", "obj_dependency_data.csv"]
