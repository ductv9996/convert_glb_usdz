FROM plattar/python-xrutils:release-1.108.3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY ./main.py .

# run the command
CMD ["python", "./main.py"]