# 🗑️ Waste Classification AI

<div align="center">

![WasteAI](https://img.shields.io/badge/WasteAI-ML%20Classification-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Machine Learning Driven Waste Classification System**

Classify organic and non-organic waste using AI-powered image recognition

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [API Documentation](#-api-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Model Training](#-model-training)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

Waste Classification AI is an intelligent system that uses machine learning to automatically classify waste images as either **organic** or **non-organic**. This project helps in effective waste management and promotes environmental sustainability through automated sorting.

### Key Highlights

- 🤖 **AI-Powered Classification**: Uses Random Forest algorithm for accurate predictions
- 🎨 **Modern Web Interface**: Beautiful, responsive UI built with HTML, CSS, and JavaScript
- 🚀 **RESTful API**: Clean backend architecture with Flask
- 📊 **Real-time Results**: Instant classification with confidence scores
- 🔒 **Secure & Scalable**: Production-ready code structure

## ✨ Features

- **Image Upload**: Drag & drop or click to upload waste images
- **Real-time Classification**: Instant AI-powered waste classification
- **Confidence Scores**: View detailed probability scores for each category
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI**: Beautiful dark theme with smooth animations
- **Error Handling**: Comprehensive error messages and validation
- **Health Monitoring**: API health check endpoints

## 🛠️ Tech Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid & Flexbox
- **JavaScript (ES6+)**: Vanilla JS with async/await
- **Responsive Design**: Mobile-first approach

### Backend
- **Python 3.8+**: Core language
- **Flask 3.0**: Web framework
- **scikit-learn**: Machine learning library
- **scikit-image**: Image processing
- **NumPy**: Numerical computations

### Machine Learning
- **Random Forest Classifier**: Main ML model
- **Image Preprocessing**: Resize and flatten operations
- **Model Persistence**: Pickle serialization

## 📁 Project Structure

```
ML-Waste-classification-/
│
├── frontend/                 # Frontend application
│   ├── index.html           # Main HTML file
│   ├── css/
│   │   └── styles.css      # Styling
│   └── js/
│       ├── app.js          # Main application logic
│       └── middleware.js   # API communication layer
│
├── backend/                 # Backend API
│   ├── app.py              # Flask application
│   ├── config.py           # Configuration settings
│   ├── model_loader.py     # Model loading utilities
│   ├── utils.py            # Helper functions
│   ├── requirements.txt    # Python dependencies
│   ├── models/             # ML model storage
│   │   └── RF_Classifier.pkl
│   └── uploads/            # Temporary file storage
│
├── test images/            # Test images for classification
│
├── waste classification organic and non organic-code.ipynb  # Training notebook
│
├── .gitignore              # Git ignore rules
├── package.json            # Project metadata
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Setup (Automated)

**Windows:**
```bash
setup.bat
run.bat
```

**macOS/Linux:**
```bash
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

### Manual Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ML-Waste-classification-.git
cd ML-Waste-classification-
```

#### Step 2: Set Up Backend

1. Create a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r backend/requirements.txt
```

3. Ensure model file exists:

Place your trained model (`RF_Classifier.pkl`) in `backend/models/` directory.

#### Step 3: Run the Application

**Terminal 1 - Start Backend:**
```bash
python backend/app.py
```
✅ Backend running at `http://localhost:5000`

**Terminal 2 - Start Frontend (Optional):**
```bash
cd frontend
python -m http.server 8000
```
✅ Frontend at `http://localhost:8000`

**Or simply open `frontend/index.html` directly in your browser!**

> 📖 **For detailed instructions, see [HOW_TO_RUN.md](HOW_TO_RUN.md)**

## 💻 Usage

### Using the Web Interface

1. **Upload Image**: 
   - Click the upload area or drag & drop an image
   - Supported formats: JPG, PNG, GIF, BMP
   - Maximum file size: 16MB

2. **Classify**: 
   - Click the "Classify Waste" button
   - Wait for the AI to process the image

3. **View Results**: 
   - See the classification result (Organic/Non-Organic)
   - View confidence scores and probability bars
   - Click "Classify Another Image" to try again

### API Usage

#### Health Check

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "service": "Waste Classification API"
}
```

#### Classify Image

```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/api/predict
```

Response:
```json
{
  "success": true,
  "prediction": "ORGANIC",
  "confidence": 95.5,
  "probabilities": {
    "ORGANIC": 95.5,
    "NONORGANIC": 4.5
  }
}
```

## 📚 API Documentation

### Endpoints

#### `GET /api/health`
Check API health and model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "service": "Waste Classification API"
}
```

#### `POST /api/predict`
Classify waste image.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `image` (file)

**Response:**
```json
{
  "success": true,
  "prediction": "ORGANIC",
  "confidence": 95.5,
  "probabilities": {
    "ORGANIC": 95.5,
    "NONORGANIC": 4.5
  }
}
```

**Error Response:**
```json
{
  "error": "Invalid file type",
  "message": "Allowed file types: png, jpg, jpeg, gif, bmp"
}
```

#### `GET /api/model/status`
Get model status information.

**Response:**
```json
{
  "is_loaded": true,
  "model_path": "backend/models/RF_Classifier.pkl",
  "model_exists": true,
  "categories": ["ORGANIC", "NONORGANIC"]
}
```

## 🧪 Model Training

The model training code is available in the Jupyter notebook: `waste classification organic and non organic-code.ipynb`

### Training Process

1. **Data Preparation**: 
   - Images are resized to 150x150x3
   - Flattened into feature vectors

2. **Model Training**:
   - Random Forest Classifier
   - Train/test split (70/30)
   - Model saved as `RF_Classifier.pkl`

3. **Model Usage**:
   - Load the trained model
   - Preprocess input images
   - Make predictions

## 🔧 Configuration

Backend configuration can be modified in `backend/config.py`:

```python
# Flask Configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True

# File Upload
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- scikit-learn team for the excellent ML library
- Flask team for the web framework
- All contributors and testers

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

<div align="center">

**Made with ❤️ for a sustainable future**

⭐ Star this repo if you find it helpful!

</div>
