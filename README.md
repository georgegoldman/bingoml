# Trash Talker
Trash Talker is an AI-powered waste sorting app that makes it easy to identify recyclable and non-recyclable items. Just snap a picture of your waste, and Trash Talker quickly identifies its category and offers options for proper disposal. You can even earn rewards for recycling and arrange pickups with local recycling stations, all through the app!

Features
- **AI-Powered Waste Classification:** Upload a picture of your waste, and the app will classify it as glass, metal, paper, plastic, or non-recyclable items using machine learning.
- **Rewards for Recycling:** Earn cash rewards for recyclable items that can be collected by local recycling stations.
- **Pickup Scheduling:** Easily schedule a pickup for recyclable waste with nearby recycling stations.
- **Smart, Sustainable, Simple:** Helps reduce waste and support sustainable practices effortlessly.

## Getting Started
Prerequisites
Python 3.7+
MongoDB Atlas for database storage
FastAPI and Uvicorn for the backend API

## Installation
Clone the Repository

```
bash
git clone git@github.com:georgegoldman/bingoml.git
cd trash-talker
```
Install Dependencies

```
bash
pip install -r requirements.txt
Set Up MongoDB Connection
```

Create a .env file in the project root and add your MongoDB URI:

```
bash
MONGO_DB_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
Run the Application
```

```
bash
./start.sh
```
The API will be accessible at http://localhost:8000.

## API Endpoints
- **POST** /classify/: Upload an image to classify the type of waste.
- **POST** /create_user/: Create a user with an email and wallet balance.
- **POST** /schedule_pickup/: Schedule a pickup for recyclable items.

## Testing with Postman
1. **Run the Server:** Start the FastAPI server by running ./start.sh.
2. **Classify Waste:** Use the POST /classify/ endpoint to upload an image and get a classification response.
3. **Create User:** Use the POST /create_user/ endpoint to create a user profile with wallet details.
4. **Schedule Pickup:** Use the POST /schedule_pickup/ endpoint to arrange for recyclable items pickup.

## Deployment
To deploy on Render:

1. Push your code to GitHub.
2. Create a new Web Service on Render and connect your GitHub repository.
3. Set environment variables, including MONGO_DB_URL.
4. Deploy the app and access it through the Render-provided URL.

## Tech Stack
- **FastAPI:** Python-based web framework for the API.
- **MongoDB:** Database to store user and wallet data.
- **scikit-image:** For image processing and resizing.
- **scikit-learn:** Machine learning model for waste classification.
- **Uvicorn:** ASGI server to run the FastAPI app.

## License
This project is licensed under the MIT License.