fetch("http://localhost:8000/auth/register", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/auth/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/auth/logout", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/auth/refresh", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/users/me", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/admin/dictionaries", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/admin/dictionaries", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/admin/dictionaries/{dictionary_id}", {
  method: "PATCH",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/admin/dictionaries/{dictionary_id}/words", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/stats/users/{user_id}", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/stats/global", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/stats/leaderboard", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/abort", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/stats", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/time", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/healthz", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/version", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games/{game_id}/state", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games/{game_id}/guess", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games/{game_id}/history", {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})
fetch("http://localhost:8000/sessions/{session_id}/games/{game_id}/abort", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username,
    full_name: fullName,
    email,
    password
  })
})