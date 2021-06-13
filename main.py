from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI

import json

from app import policy_handler

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
    # print("AdmissionReview Object received is: ", json.dumps(admission_review))
    object_kind = admission_review["request"]["kind"]["kind"]

    # v1.AdmissionReview or v1beta1.AdmissionReview
    api_version = admission_review["apiVersion"]
    # print("Kuberentes Object is: ", object_kind)

    if(object_kind.lower() == "admissionpolicy"):
        print("AdmissionReview Object: ", json.dumps(admission_review))
        policy_handler.create_update(admission_review["request"]["object"])
    if(object_kind.lower() == "pod"):
        print("AdmissionReview Object: ", json.dumps(admission_review))
        policy_handler.resource(admission_review["request"]["object"])

    res = {
        "apiVersion": api_version,  # Must return same that we get
        "kind": "AdmissionReview",
        "response": {
            # Must return same that we get
            "uid": admission_review["request"]["uid"],
            "allowed": True,
            "status": {
                "code": 200,
                "message": "Allowing everything for now"
            }
        }
    }
    return res

