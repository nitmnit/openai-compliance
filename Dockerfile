FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye
USER vscode
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
