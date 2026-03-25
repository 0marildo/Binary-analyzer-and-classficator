# Binary Analyzer & Classifier

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

An ML-powered tool that analyzes binary files using statistical feature extraction and DBSCAN clustering to classify binary data blocks.

## Features

- **File Upload** -- Upload `.bin` files through a clean drag-and-drop interface
- **Statistical Feature Extraction** -- Computes entropy, byte-zero ratio, unique byte ratio, and variance for each data block
- **DBSCAN Clustering** -- Groups similar blocks using density-based spatial clustering with standardized features
- **2D Scatter Plot Visualization** -- Generates an interactive scatter plot of entropy vs. variance colored by cluster
- **Block Classification** -- Classifies blocks into categories: headers, raw data, and offsets

## Architecture

```
.bin file
   |
   v
[Split into 32-byte blocks]
   |
   v
[Feature Extraction]  -->  entropy, zero-ratio, unique-ratio, variance
   |
   v
[StandardScaler + DBSCAN Clustering]
   |
   v
[Classification + Plot Generation]
   |
   v
JSON response (cluster labels, summary counts, base64 scatter plot)
```

The backend receives a binary file, splits it into fixed-size blocks (32 bytes), extracts four statistical features per block, normalizes the features with `StandardScaler`, and runs DBSCAN (`eps=0.2`, `min_samples=3`) to identify clusters. Blocks labeled as noise (`cluster -1`) are classified as offsets, while clustered blocks are classified as raw data. The result includes cluster assignments, a summary, and a base64-encoded scatter plot.

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

### Environment Variables

Copy the `.env.example` file and adjust values as needed:

```bash
cp .env.example .env
```

See `.env.example` for all available configuration options.

## API Documentation

### `POST /api/v1/analyze`

Accepts a `.bin` file upload and returns analysis results.

**Request:** `multipart/form-data` with a `file` field containing a `.bin` file (max 50MB).

**Response:**
```json
{
  "num_blocks": 1024,
  "clusters": [0, 0, 1, -1, 0, ...],
  "plot": "data:image/png;base64,...",
  "summary": {
    "header": 0,
    "raw_data": 800,
    "offset": 224
  }
}
```

### `GET /health`

Returns the API health status.

**Response:**
```json
{
  "status": "OK"
}
```

## Project Structure

```
Binary-analyzer-and-classficator/
├── backend/
│   ├── api/routes/api.py        # FastAPI route definitions
│   ├── ml/
│   │   ├── analyzer.py          # Main analysis pipeline
│   │   ├── clustering.py        # DBSCAN clustering logic
│   │   ├── features.py          # Feature extraction functions
│   │   └── plot.py              # Scatter plot generation
│   ├── schemas/analyze.py       # Pydantic response models
│   ├── services/binary_analyzer.py
│   ├── tests/
│   ├── main.py                  # FastAPI app entrypoint
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/          # React UI components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── infra/services/      # API service layer
│   │   └── pages/               # Page components
│   ├── package.json
│   └── vite.config.js
├── .github/workflows/ci.yml     # CI pipeline
├── .env.example
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).
