# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.1-slim-buster
LABEL maintainer="Kumar Aditya <rahuladitya303@gmail.com>"
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["/bin/sh","docker-entrypoint.sh"]
