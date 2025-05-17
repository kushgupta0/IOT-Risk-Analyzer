from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from scanner import search_cves
from risk_score import calculate_risk_score

app = FastAPI()

class DeviceInfo(BaseModel):
    device_name: str
    model: Optional[str] = None
    firmware: Optional[str] = None

@app.post("/analyze_device")
def analyze_device(device: DeviceInfo):
    try:
        cve_list = search_cves(device.device_name, device.model)
        risk_score, summary = calculate_risk_score(cve_list)

        return {
            "device": device,
            "cves_found": cve_list,
            "risk_score": risk_score,
            "risk_level": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
