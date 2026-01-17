import React from 'react'
import { createRoot } from 'react-dom/client'
import Login from './components/Login.jsx'

function App() {
  return (
    <div style={{ padding: 24 }}>
      <h2>Hangman Frontend</h2>
      <Login />
    </div>
  )
}

const root = createRoot(document.getElementById('root'))
root.render(<App />)
