/**
 * Main Application Logic
 * Handles UI interactions and coordinates with middleware
 */

// Initialize API Middleware
const api = new APIMiddleware('http://localhost:5000');

// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const removeBtn = document.getElementById('removeBtn');
const classifyBtn = document.getElementById('classifyBtn');
const resultsSection = document.getElementById('resultsSection');
const loadingOverlay = document.getElementById('loadingOverlay');
const resetBtn = document.getElementById('resetBtn');

// State
let currentFile = null;

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

/**
 * Initialize application
 */
async function initializeApp() {
    setupEventListeners();
    await checkBackendHealth();
}

/**
 * Setup event listeners
 */
function setupEventListeners() {
    // Upload area click
    uploadArea.addEventListener('click', () => {
        fileInput.click();
    });

    // File input change
    fileInput.addEventListener('change', handleFileSelect);

    // Drag and drop
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);

    // Remove image
    removeBtn.addEventListener('click', removeImage);

    // Classify button
    classifyBtn.addEventListener('click', handleClassify);

    // Reset button
    resetBtn.addEventListener('click', resetApp);
}

/**
 * Handle file selection
 */
function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        processFile(file);
    }
}

/**
 * Handle drag over
 */
function handleDragOver(event) {
    event.preventDefault();
    event.stopPropagation();
    uploadArea.classList.add('dragover');
}

/**
 * Handle drag leave
 */
function handleDragLeave(event) {
    event.preventDefault();
    event.stopPropagation();
    uploadArea.classList.remove('dragover');
}

/**
 * Handle drop
 */
function handleDrop(event) {
    event.preventDefault();
    event.stopPropagation();
    uploadArea.classList.remove('dragover');

    const file = event.dataTransfer.files[0];
    if (file) {
        processFile(file);
    }
}

/**
 * Process selected file
 */
function processFile(file) {
    // Validate file
    const validation = api.validateImageFile(file);
    if (!validation.valid) {
        showError(validation.error);
        return;
    }

    currentFile = file;

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewSection.style.display = 'flex';
        uploadArea.style.display = 'none';
        hideError();
    };
    reader.readAsDataURL(file);
}

/**
 * Remove image
 */
function removeImage() {
    currentFile = null;
    fileInput.value = '';
    previewSection.style.display = 'none';
    uploadArea.style.display = 'block';
    resultsSection.style.display = 'none';
    hideError();
}

/**
 * Handle classify button click
 */
async function handleClassify() {
    if (!currentFile) {
        showError('Please select an image first');
        return;
    }

    // Show loading
    showLoading();

    try {
        // Classify image
        const result = await api.classifyWaste(currentFile);

        if (result.success) {
            displayResults(result.data);
        } else {
            showError(result.error || 'Classification failed. Please try again.');
        }
    } catch (error) {
        showError(error.message || 'An unexpected error occurred');
    } finally {
        hideLoading();
    }
}

/**
 * Display classification results
 */
function displayResults(data) {
    const { prediction, confidence, probabilities } = data;

    // Update result badge
    const resultBadge = document.getElementById('resultBadge');
    resultBadge.className = `result-badge ${prediction.toLowerCase()}`;
    resultBadge.innerHTML = `
        <span class="badge-label">${prediction}</span>
        <span class="badge-confidence">${confidence}%</span>
    `;

    // Update confidence bars
    const organicConfidence = probabilities.ORGANIC || 0;
    const nonOrganicConfidence = probabilities.NONORGANIC || 0;

    document.getElementById('organicConfidence').textContent = `${organicConfidence}%`;
    document.getElementById('nonOrganicConfidence').textContent = `${nonOrganicConfidence}%`;

    // Animate progress bars
    setTimeout(() => {
        document.getElementById('organicProgress').style.width = `${organicConfidence}%`;
        document.getElementById('nonOrganicProgress').style.width = `${nonOrganicConfidence}%`;
    }, 100);

    // Show results section
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Reset application state
 */
function resetApp() {
    removeImage();
    resultsSection.style.display = 'none';
}

/**
 * Show loading overlay
 */
function showLoading() {
    loadingOverlay.style.display = 'flex';
}

/**
 * Hide loading overlay
 */
function hideLoading() {
    loadingOverlay.style.display = 'none';
}

/**
 * Show error message
 */
function showError(message) {
    // Create or get error element
    let errorEl = document.querySelector('.error-message');
    if (!errorEl) {
        errorEl = document.createElement('div');
        errorEl.className = 'error-message';
        uploadArea.parentElement.appendChild(errorEl);
    }

    errorEl.textContent = message;
    errorEl.classList.add('show');

    // Auto-hide after 5 seconds
    setTimeout(() => {
        hideError();
    }, 5000);
}

/**
 * Hide error message
 */
function hideError() {
    const errorEl = document.querySelector('.error-message');
    if (errorEl) {
        errorEl.classList.remove('show');
    }
}

/**
 * Check backend health
 */
async function checkBackendHealth() {
    try {
        const result = await api.checkHealth();
        if (!result.success) {
            console.warn('Backend health check failed:', result.error);
            const errorMsg = '⚠️ Backend server not running! Please start it with: python backend/app.py';
            showError(errorMsg);
            
            // Add connection status indicator
            addConnectionStatus(false);
        } else {
            addConnectionStatus(true);
            console.log('✅ Backend connected successfully');
        }
    } catch (error) {
        console.error('Health check error:', error);
        const errorMsg = '⚠️ Cannot connect to backend server. Please ensure it is running on http://localhost:5000';
        showError(errorMsg);
        addConnectionStatus(false);
    }
}

/**
 * Add connection status indicator
 */
function addConnectionStatus(connected) {
    // Remove existing status if any
    const existing = document.querySelector('.connection-status');
    if (existing) existing.remove();
    
    const status = document.createElement('div');
    status.className = `connection-status ${connected ? 'connected' : 'disconnected'}`;
    status.innerHTML = connected 
        ? '✅ Backend Connected' 
        : '❌ Backend Disconnected - Start server with: python backend/app.py';
    status.style.cssText = `
        position: fixed;
        top: 10px;
        right: 10px;
        padding: 10px 15px;
        border-radius: 5px;
        font-size: 12px;
        z-index: 1000;
        ${connected 
            ? 'background: #10b981; color: white;' 
            : 'background: #ef4444; color: white;'
        }
    `;
    document.body.appendChild(status);
    
    if (connected) {
        setTimeout(() => status.remove(), 3000);
    }
}
