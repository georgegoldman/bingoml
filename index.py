import pickle
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from skimage.io import imread
from skimage.transform import resize
import numpy as np


app = FastAPI()

# Load the trained model
with open('./model.p', 'rb') as model_file:
    model = pickle.load(model_file)


# Define categories based on your training labels
categories = ['glass', 'metal', 'paper', 'plastic']

@app.post("/classify/")
async def classify_image(file: UploadFile = File(...)):
    # Read and process the uploaded image
    try:
        image = imread(file.file)
        image_resized = resize(image, (15, 15))
        image_flattened = image_resized.flatten().reshape(1, -1)


        # Predict using the loaded model
        prediction  = model.predict(image_flattened)

        # Map the prediction to the corresponding category
        prediction_label = categories[prediction[0]]
        return JSONResponse(content={"prediction": prediction_label})
    
    except Exception as e:
        return JSONResponse(content={"error ": str(e) }, status_code=500)
    


# Start the server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

