import { useState } from "react"
import { AuthLayout } from "../components/AuthLayout"
import { Input } from "../components/Input"
import { Button } from "../components/Button"

function Login() {
  // STATE: Store user input
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [errors, setErrors] = useState({})
  const [isLoading, setIsLoading] = useState(false)

  // VALIDATION
  const validateForm = () => {
    const newErrors = {}
    
    if (!email.includes("@")) {
      newErrors.email = "Please enter a valid email"
    }
    
    if (password.length < 8) {
      newErrors.password = "Password must be at least 8 characters"
    }
    
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  // SUBMIT HANDLER
  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!validateForm()) {
      return
    }
    
    setIsLoading(true)
    
    try {
      // TODO: Replace with your actual login API
      const response = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          username: email,  // Backend expects "username" field
          password 
        })
      })
      
      if (response.ok) {
        const data = await response.json()
        // Store the authentication token
        localStorage.setItem("authToken", data.access_token)
        
        alert("Login successful!")
        // Redirect to dashboard
        window.location.href = "/dashboard"
      } else {
        alert("Invalid email or password")
      }
    } catch (error) {
      alert("Network error. Please try again.")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <AuthLayout>
      <form onSubmit={handleSubmit} className="flex flex-col gap-6">
        <div className="flex flex-col items-center gap-2 text-center">
          <h1 className="text-2xl font-bold">Login to your account</h1>
        </div>

        <div className="grid gap-4">
          {/* EMAIL INPUT */}
          <div className="grid gap-2">
            <label className="text-sm font-medium">Email</label>
            <Input
              type="email"
              placeholder="user@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            {errors.email && (
              <p className="text-xs text-red-500">{errors.email}</p>
            )}
          </div>

          {/* PASSWORD INPUT */}
          <div className="grid gap-2">
            <div className="flex items-center justify-between">
              <label className="text-sm font-medium">Password</label>
              <a 
                href="/recover-password" 
                className="text-sm text-primary hover:underline"
              >
                Forgot password?
              </a>
            </div>
            <Input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            {errors.password && (
              <p className="text-xs text-red-500">{errors.password}</p>
            )}
          </div>

          {/* SUBMIT BUTTON */}
          <Button type="submit" disabled={isLoading}>
            {isLoading ? "Logging in..." : "Log In"}
          </Button>
        </div>

        <div className="text-center text-sm">
          Don't have an account yet?{" "}
          <a href="/signup" className="underline text-primary">
            Sign up
          </a>
        </div>
      </form>
    </AuthLayout>
  )
}

export default Login