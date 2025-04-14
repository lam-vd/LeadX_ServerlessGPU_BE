from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)

class GPUJobService:

    @staticmethod
    def create_job(gpu_type: str, image_path: str) -> dict:
        url = f"{settings.GPU_SERVERLESS_API_BASE_URL}/job/run"
        payload = {
            "gpu_type": gpu_type,
            "image_path": image_path
        }
        try:
            response = requests.post(
                url,
                json=payload,
                headers={"accept": "application/json", "Content-Type": "application/json"},
                timeout=20
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to create GPU job: {str(e)}")
            raise Exception("Failed to create GPU job")

    @staticmethod
    def get_job_status(job_id: str) -> dict:
        url = f"{settings.GPU_SERVERLESS_API_BASE_URL}/job/status"
        params = {"job_id": job_id}
        try:
            response = requests.get(
                url,
                params=params,
                headers={"accept": "application/json"},
                timeout=20
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get job status: {str(e)}")
            raise Exception("Failed to get job status")

    @staticmethod
    def delete_job(job_id: str) -> dict:
        url = f"{settings.GPU_SERVERLESS_API_BASE_URL}/job/delete"
        payload = {"job_id": job_id}
        try:
            response = requests.post(
                url,
                json=payload,
                headers={"accept": "application/json", "Content-Type": "application/json"},
                timeout=20
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to delete GPU job: {str(e)}")
            raise Exception("Failed to delete GPU job")