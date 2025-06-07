import os
from datetime import datetime
from django.conf import settings
from core.utils.docker_utils import DockerUtils
from core.models.user import hash_user_id
from core.utils.dockerfile_generator import generate_dockerfile_content
import logging

logger = logging.getLogger(__name__)
class TaskService:
    @staticmethod
    def save_source_code(user, source_code):
        hashed_id = hash_user_id(user.id)
        now = datetime.now()
        user_dir = os.path.join(settings.BASE_DIR, "task_job", str(now.year), str(now.month), f"user_{hashed_id}")
        os.makedirs(user_dir, exist_ok=True)
        file_path = os.path.join(user_dir, f"user_{hashed_id}_app.py")
        with open(file_path, "w") as f:
            f.write(source_code)
        return file_path

    @staticmethod
    def create_dockerfile(file_path):
        dockerfile_content = generate_dockerfile_content(file_path)
        dockerfile_path = os.path.join(os.path.dirname(file_path), "Dockerfile")
        with open(dockerfile_path, "w") as f:
            f.write(dockerfile_content)

        return dockerfile_path

    @staticmethod
    def build_and_push_image(user, task_name, file_path):
        hashed_id = hash_user_id(user.id)
        image_name = f"user_{hashed_id}_{task_name.lower().replace(' ', '_')}:latest"
        registry_url = settings.DOCKER_REGISTRY_URL
        full_image_path = f"{registry_url}/{image_name}"
        DockerUtils.build_image(image_name, os.path.dirname(file_path))
        DockerUtils.tag_image(image_name, full_image_path)
        DockerUtils.push_image(full_image_path)

        return full_image_path