from fastapi import FastAPI, File, UploadFile
from app.services.detection_service import detect_holes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Kumaş delik tespit API'si şu anda çalışıyor."}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image, detections = detect_holes(image_bytes)
    return {"detections": detections, "image": processed_image}
