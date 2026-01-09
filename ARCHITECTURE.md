# Architecture Documentation

## System Architecture

The Waste Classification AI system follows a three-tier architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   HTML/CSS   │  │  JavaScript  │  │  Middleware  │ │
│  │   (UI/UX)    │  │  (Logic)     │  │  (API Calls) │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                          │
                          │ HTTP/REST API
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   Backend Layer (Flask)                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   Routes     │  │   Utils      │  │ Model Loader │ │
│  │  (Endpoints) │  │ (Processing) │  │  (ML Model)  │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                          │
                          │ Model Inference
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  Machine Learning Layer                   │
│  ┌────────────────────────────────────────────────────┐ │
│  │         Random Forest Classifier                    │ │
│  │         (RF_Classifier.pkl)                         │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## Component Details

### Frontend Layer

#### HTML (`frontend/index.html`)
- Semantic HTML5 structure
- Accessible markup
- Responsive layout foundation

#### CSS (`frontend/css/styles.css`)
- Modern CSS3 with custom properties
- Responsive design (mobile-first)
- Dark theme with gradient accents
- Smooth animations and transitions

#### JavaScript

**App Logic (`frontend/js/app.js`)**
- UI event handling
- File upload management
- Drag & drop functionality
- Result display
- Error handling

**Middleware (`frontend/js/middleware.js`)**
- API communication layer
- Request/response handling
- File validation
- Error management
- Progress tracking

### Backend Layer

#### Flask Application (`backend/app.py`)
- Main application entry point
- Route definitions
- Request handling
- Response formatting

#### Configuration (`backend/config.py`)
- Centralized configuration
- Environment variables support
- Path management
- Constants definition

#### Utilities (`backend/utils.py`)
- Image preprocessing
- File validation
- Directory management
- Helper functions

#### Model Loader (`backend/model_loader.py`)
- Model loading and management
- Prediction interface
- Status monitoring
- Error handling

### Machine Learning Layer

#### Model
- **Algorithm**: Random Forest Classifier
- **Input**: 150x150x3 flattened image (67,500 features)
- **Output**: Binary classification (Organic/Non-Organic)
- **Format**: Pickle (.pkl)

#### Preprocessing Pipeline
1. Image reading (scikit-image)
2. Resize to 150x150x3
3. Flatten to 1D array
4. Reshape for model input

## Data Flow

### Classification Request Flow

```
User Uploads Image
       │
       ▼
Frontend Validation (File type, size)
       │
       ▼
Middleware API Call (POST /api/predict)
       │
       ▼
Backend Receives Request
       │
       ▼
File Validation & Security Check
       │
       ▼
Save Temporary File
       │
       ▼
Image Preprocessing (Resize, Flatten)
       │
       ▼
Model Prediction (Random Forest)
       │
       ▼
Format Response (Category, Confidence, Probabilities)
       │
       ▼
Delete Temporary File
       │
       ▼
Return JSON Response
       │
       ▼
Frontend Displays Results
```

## API Design

### RESTful Endpoints

1. **GET /api/health**
   - Purpose: Health check
   - Response: Service status, model status

2. **POST /api/predict**
   - Purpose: Classify waste image
   - Input: Multipart form data (image file)
   - Output: Classification result with confidence

3. **GET /api/model/status**
   - Purpose: Model information
   - Response: Model loading status, categories

## Security Considerations

1. **File Upload Security**
   - File type validation
   - File size limits
   - Secure filename handling
   - Temporary file cleanup

2. **CORS Configuration**
   - Configurable origins
   - Secure defaults

3. **Error Handling**
   - No sensitive information in errors
   - Proper HTTP status codes
   - Logging for debugging

## Scalability Considerations

1. **Stateless Design**
   - No session management
   - Each request is independent

2. **Model Caching**
   - Model loaded once at startup
   - In-memory prediction

3. **File Management**
   - Temporary files cleaned up immediately
   - No persistent storage needed

4. **Future Enhancements**
   - Model versioning
   - Batch processing
   - Caching predictions
   - Database integration

## Technology Choices

### Why Flask?
- Lightweight and flexible
- Easy to deploy
- Good for ML APIs
- Extensive ecosystem

### Why Random Forest?
- Good accuracy for image classification
- Fast inference
- Handles high-dimensional data
- Interpretable results

### Why Vanilla JavaScript?
- No build step required
- Fast loading
- Easy to understand
- Modern ES6+ features sufficient

## Deployment Considerations

### Development
- Flask debug mode
- Local file storage
- Single-threaded

### Production
- Use production WSGI server (Gunicorn, uWSGI)
- Environment variables for configuration
- Proper logging
- Health check monitoring
- Load balancing (if needed)

## Future Improvements

1. **Model Enhancements**
   - Deep learning models (CNN)
   - Transfer learning
   - Model ensemble

2. **Frontend Enhancements**
   - Progressive Web App (PWA)
   - Offline support
   - Image editing tools

3. **Backend Enhancements**
   - Database for history
   - User authentication
   - Batch processing API
   - Model versioning

4. **Infrastructure**
   - Docker containerization
   - CI/CD pipeline
   - Cloud deployment
   - Monitoring and analytics
