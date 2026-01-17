const API_URL = 'http://localhost:8000/api/v1';

function getToken() {
    return localStorage.getItem('access_token');
}

function setToken(token) {
    localStorage.setItem('access_token', token);
}

function removeToken() {
    localStorage.removeItem('access_token');
}

async function apiRequest(endpoint, method = 'GET', data = null, auth = false) {
    const headers = {
        'Content-Type': 'application/json'
    };

    if (auth) {
        const token = getToken();
        if (!token) {
            window.location.href = 'login.html';
            return;
        }
        headers['Authorization'] = `Bearer ${token}`;
    }

    const options = {
        method,
        headers,
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    // Handle form-urlencoded for login
    if (endpoint === '/login/access-token') {
        const formData = new URLSearchParams();
        for (const key in data) {
            formData.append(key, data[key]);
        }
        options.body = formData;
        delete headers['Content-Type']; // Let browser set it
    }

    try {
        const response = await fetch(`${API_URL}${endpoint}`, options);
        if (response.status === 401 && auth) {
            removeToken();
            window.location.href = 'login.html';
            return;
        }
        
        const responseData = await response.json();
        
        if (!response.ok) {
            throw new Error(responseData.detail || 'Something went wrong');
        }
        
        return responseData;
    } catch (error) {
        throw error;
    }
}
