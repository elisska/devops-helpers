FROM python:3.7

# this will create /my_application directory in Docker image
WORKDIR /my_application

# this will install some packages
RUN pip install networkx dash plotly

# this will copy application code to working directory
#COPY . /my_application/
COPY . .

# this command is started when container is ran
CMD python GraphAnalysis.py obj_dependency_data.csv
