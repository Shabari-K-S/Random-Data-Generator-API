from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from faker import Faker
import random
from datetime import datetime

app = FastAPI(title="Random Data Generator API")

faker = Faker()

SUPPORTED_TYPES = {
    "email", "uuid", "date", "name", "sentence", "number", "ip_address"
}


class DataResponse(BaseModel):
    data_type: str
    generated_items: List[str]


@app.get("/generate", response_model=DataResponse)
def generate_data(
    type: str = Query(..., description="Type of data to generate"),
    count: int = Query(1, ge=1, le=100, description="Number of items to generate"),
    format: Optional[str] = Query(None, description="Format for date/number types")
):
    type = type.lower()
    if type not in SUPPORTED_TYPES:
        raise HTTPException(status_code=400, detail=f"Unsupported type: {type}")

    result = []

    for _ in range(count):
        if type == "email":
            result.append(faker.email())

        elif type == "uuid":
            result.append(str(uuid4()))

        elif type == "date":
            if format:
                try:
                    result.append(faker.date(pattern=format))
                except Exception:
                    raise HTTPException(status_code=400, detail="Invalid date format")
            else:
                result.append(faker.date())

        elif type == "name":
            result.append(faker.name())

        elif type == "sentence":
            result.append(faker.sentence())

        elif type == "number":
            if format == "float":
                result.append(str(round(random.uniform(1, 1000), 2)))
            else:
                result.append(str(random.randint(1, 1000)))

        elif type == "ip_address":
            result.append(faker.ipv4())

    return DataResponse(data_type=type, generated_items=result)
