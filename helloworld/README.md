# Google App Engine Python Flask Application

## Overview

This is a Python Flask web application designed to run on Google Cloud Platform's App Engine Standard Environment. The application demonstrates basic cloud deployment concepts and provides a functional web interface.

## Files

- **main.py**: Flask application with routes for the main page and health check
- **app.yaml**: App Engine configuration file specifying runtime, scaling, and environment settings
- **requirements.txt**: Python package dependencies

## Local Development

### Prerequisites
- Python 3.12
- pip (Python package manager)

### Setup

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and visit: `http://localhost:8080`

## Deployment to App Engine

1. Ensure Google Cloud SDK is installed and authenticated
2. Set your GCP project:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```
3. Deploy:
   ```bash
   gcloud app deploy
   ```
4. View your application:
   ```bash
   gcloud app browse
   ```

## Application Endpoints

- **GET /** - Main page with application information
- **GET /health** - Health check endpoint (returns JSON)

## Configuration

The `app.yaml` file configures:
- Runtime: Python 3.12
- Scaling: Automatic scaling (1-10 instances)
- Instance class: F1 (free tier eligible)

## Student Information

- **Name:** CHRIS MUCHEMI
- **Registration Number:** 23/07447
- **Course:** CPP 3102 - General

