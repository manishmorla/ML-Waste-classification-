/**
 * Middleware Layer for API Communication
 * Handles all API requests and responses between frontend and backend
 */

class APIMiddleware {
    constructor(baseURL = 'http://localhost:5000') {
        this.baseURL = baseURL;
        this.endpoints = {
            health: '/api/health',
            predict: '/api/predict',
            modelStatus: '/api/model/status'
        };
    }

    /**
     * Generic fetch wrapper with error handling
     * @param {string} url - API endpoint URL
     * @param {Object} options - Fetch options
     * @returns {Promise} - Response data or error
     */
    async request(url, options = {}) {
        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    ...options.headers,
                },
                mode: 'cors',
                credentials: 'omit'
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.message || errorData.error || `HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Request Error:', error);
            
            // Provide more helpful error messages
            if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
                throw new Error('Cannot connect to backend server. Please ensure the backend is running on http://localhost:5000');
            }
            
            throw error;
        }
    }

    /**
     * Check backend health status
     * @returns {Promise<Object>} - Health status response
     */
    async checkHealth() {
        try {
            const response = await this.request(`${this.baseURL}${this.endpoints.health}`);
            return {
                success: true,
                data: response
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Get model status
     * @returns {Promise<Object>} - Model status response
     */
    async getModelStatus() {
        try {
            const response = await this.request(`${this.baseURL}${this.endpoints.modelStatus}`);
            return {
                success: true,
                data: response
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Classify waste image
     * @param {File} imageFile - Image file to classify
     * @param {Function} onProgress - Progress callback (optional)
     * @returns {Promise<Object>} - Prediction response
     */
    async classifyWaste(imageFile, onProgress = null) {
        try {
            // Validate file
            if (!imageFile) {
                throw new Error('No image file provided');
            }

            // Validate file type
            const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp'];
            if (!allowedTypes.includes(imageFile.type)) {
                throw new Error('Invalid file type. Please upload JPG, PNG, GIF, or BMP image.');
            }

            // Validate file size (16MB max)
            const maxSize = 16 * 1024 * 1024; // 16MB
            if (imageFile.size > maxSize) {
                throw new Error('File size too large. Maximum size is 16MB.');
            }

            // Create FormData
            const formData = new FormData();
            formData.append('image', imageFile);

            // Simulate progress if callback provided
            if (onProgress) {
                onProgress(0.3);
                setTimeout(() => onProgress(0.6), 200);
                setTimeout(() => onProgress(0.9), 400);
            }

            // Make API request
            const response = await this.request(`${this.baseURL}${this.endpoints.predict}`, {
                method: 'POST',
                body: formData
            });

            if (onProgress) {
                onProgress(1.0);
            }

            return {
                success: true,
                data: response
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Validate image file before upload
     * @param {File} file - File to validate
     * @returns {Object} - Validation result
     */
    validateImageFile(file) {
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp'];
        const maxSize = 16 * 1024 * 1024; // 16MB

        if (!file) {
            return {
                valid: false,
                error: 'No file selected'
            };
        }

        if (!allowedTypes.includes(file.type)) {
            return {
                valid: false,
                error: 'Invalid file type. Please upload JPG, PNG, GIF, or BMP image.'
            };
        }

        if (file.size > maxSize) {
            return {
                valid: false,
                error: 'File size too large. Maximum size is 16MB.'
            };
        }

        return {
            valid: true,
            error: null
        };
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = APIMiddleware;
}
