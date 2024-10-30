import httpx
from typing import List, Optional, Dict
import logging
from fastapi import HTTPException

class LiteraryVaultClient:
    def __init__(self):
        self.base_url = "https://exios66.github.io/Literary-Vault/api/v1"
        self.logger = logging.getLogger(__name__)

    async def get_questions(
        self, 
        category: str, 
        limit: Optional[int] = 10,
        random: Optional[bool] = True
    ) -> List[Dict]:
        """
        Fetch questions from Literary Vault API
        """
        try:
            params = {
                "limit": limit,
                "random": random
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/questions/{category}",
                    params=params
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"Error fetching questions: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to fetch questions")

    async def randomize_questions(
        self,
        category: str,
        count: Optional[int] = 5,
        seed: Optional[int] = None
    ) -> List[Dict]:
        """
        Get randomized questions from Literary Vault API
        """
        try:
            data = {
                "category": category,
                "count": count
            }
            if seed is not None:
                data["seed"] = seed

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/questions/randomize",
                    json=data
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"Error randomizing questions: {str(e)}")
            raise HTTPException(status_code=500, detail="Failed to randomize questions") 