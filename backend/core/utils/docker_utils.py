import subprocess
from django.conf import settings

class DockerUtils:
    @staticmethod
    def login_to_registry():
        command = [
            "docker", "login",
            settings.DOCKER_REGISTRY_URL,
            "--username", settings.DOCKER_REGISTRY_USERNAME,
            "--password-stdin"
        ]
        try:
            process = subprocess.run(
                command,
                input=settings.DOCKER_REGISTRY_PASSWORD.encode(),
                check=True,
                capture_output=True
            )
            print(process.stdout.decode())
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to login to registry: {e.stderr.decode()}")

    @staticmethod
    def build_image(image_name, build_context):
        command = ["docker", "build", "-t", image_name, build_context]
        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)

    @staticmethod
    def tag_image(image_name, full_image_path):
        command = ["docker", "tag", image_name, full_image_path]
        subprocess.run(command, check=True)

    @staticmethod
    def push_image(full_image_path):
        DockerUtils.login_to_registry()
        command = ["docker", "push", full_image_path]
        try:
            subprocess.run(command, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to push image: {e.stderr.decode()}")