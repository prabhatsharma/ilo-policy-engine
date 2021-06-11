from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



@app.get("/")
async def read_root():
    res = {
        "what": "ILO validation webhook admission controller",
        "where": "/validate will accept POST data ",
        "docs": "Official k8s at https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/"
    }
    return res


@app.post("/validate")
async def validate(admission_review: dict):
    print("AdmissionReview Object received is: ", admission_review)
    res = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": admission_review["request"]["uid"],
            "allowed": True,
            "status": {
                "code": 200,
                "message": "Allowing everything for now"
            }
        }
    }
    return res


