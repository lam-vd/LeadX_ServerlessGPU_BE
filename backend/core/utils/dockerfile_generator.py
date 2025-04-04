import os

def generate_dockerfile_content(file_path):
    return f"""
    FROM python:3.11-slim
    WORKDIR /app
    COPY ./{os.path.basename(file_path)} /app/
    CMD ["python", "/app/{os.path.basename(file_path)}"]
    """ 