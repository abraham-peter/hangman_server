// Auto-detect API base URL: use same origin in production, localhost:8000 in development
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
  ? 'http://localhost:8000' 
  : window.location.origin;

async function apiRequest(path, method = 'GET', body = null, options = { json: true }) {
  const url = API_BASE + path;
  const opts = {
    method,
    credentials: 'include', // include cookies for auth
    headers: {},
  };

  if (body != null) {
    if (options.json) {
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(body);
    } else {
      opts.headers['Content-Type'] = 'application/x-www-form-urlencoded';
      opts.body = body; // already encoded string
    }
  }

  const res = await fetch(url, opts);
  const contentType = res.headers.get('content-type') || '';
  let data = null;
  if (contentType.includes('application/json')) {
    data = await res.json();
  } else {
    data = await res.text();
  }

  if (!res.ok) {
    const msg = data && (data.detail || data.message) ? (data.detail || data.message) : (typeof data === 'string' ? data : 'Request failed');
    throw new Error(msg);
  }

  return data;
}

// Convenience helpers
async function register({ email, password, full_name }) {
  // backend expects username as the unique identifier (we use email)
  return apiRequest('/auth/register', 'POST', { username: email, email, full_name, password });
}

async function login(username, password) {
  // OAuth2PasswordRequestForm expects form urlencoded data
  const form = new URLSearchParams();
  form.append('username', username);
  form.append('password', password);
  return apiRequest('/auth/login', 'POST', form.toString(), { json: false });
}

async function logout() {
  return apiRequest('/auth/logout', 'POST', null);
}

async function getCurrentUser() {
  return apiRequest('/users/me', 'GET', null);
}

async function getLeaderboard(limit = 10) {
  return apiRequest(`/stats/leaderboard?limit=${limit}`, 'GET', null);
}

async function getUserStats(userId, period = 'all') {
  return apiRequest(`/stats/users/${userId}?period=${period}`, 'GET', null);
}

// Export to window so inline scripts can use them
window.apiRequest = apiRequest;
window.register = register;
window.login = login;
window.logout = logout;
window.getCurrentUser = getCurrentUser;
window.getLeaderboard = getLeaderboard;
window.getUserStats = getUserStats;