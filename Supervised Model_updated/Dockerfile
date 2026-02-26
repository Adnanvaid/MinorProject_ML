# use python 3.11 as base image
FROM python:3.11-slim

# set working directory
WORKDIR /api

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of application code
COPY . .

# expose the application port
EXPOSE 8000

# command to start fastapi application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]