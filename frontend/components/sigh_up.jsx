import { useState } from "react"
import { AuthLayout } from "../components/AuthLayout"
import { Input } from "../components/Input"
import { Button } from "../components/Button"

function SignUp() {
  // STATE: This stores what the user types
  const [fullName, setFullName] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")
  const [errors, setErrors] = useState({})
  const [isLoading, setIsLoading] = useState(false)

  // VALIDATION: Check if inputs are correct
  const validateForm = () => {
    const newErrors = {}
    
    if (!fullName.trim()) {
      newErrors.fullName = "Full Name is required"
    }
    
    if (!email.includes("@")) {
      newErrors.email = "Please enter a valid email"
    }
    
    if (password.length < 8) {
      newErrors.password = "Password must be at least 8 characters"
    }
    
    if (password !== confirmPassword) {
      newErrors.confirmPassword = "Passwords don't match"
    }
    
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  // SUBMIT: What happens when user clicks "Sign Up"
  const handleSubmit = async (e) => {
    e.preventDefault() // Stop page from refreshing
    
    if (!validateForm()) {
      return // Stop if validation fails
    }
    
    setIsLoading(true)
    
    try {
      // TODO: Replace this with your actual API call
      const response = await fetch("/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          full_name: fullName, 
          email, 
          password 
        })
      })
      
      if (response.ok) {
        alert("Account created! Redirecting to login...")
        // Redirect to login page
        window.location.href = "/login"
      } else {
        alert("Sign up failed. Please try again.")
      }
    } catch (error) {
      alert("Network error. Please check your connection.")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <AuthLayout>
      <form onSubmit={handleSubmit} className="flex flex-col gap-6">
        <div className="flex flex-col items-center gap-2 text-center">
          <h1 className="text-2xl font-bold">Create an account</h1>
        </div>

        <div className="grid gap-4">
          {/* FULL NAME INPUT */}
          <div className="grid gap-2">
            <label className="text-sm font-medium">Full Name</label>
            <Input
              type="text"
              placeholder="John Doe"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
            />
            {errors.fullName && (
              <p className="text-xs text-red-500">{errors.fullName}</p>
            )}
          </div>

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
            <label className="text-sm font-medium">Password</label>
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

          {/* CONFIRM PASSWORD INPUT */}
          <div className="grid gap-2">
            <label className="text-sm font-medium">Confirm Password</label>
            <Input
              type="password"
              placeholder="Confirm Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
            {errors.confirmPassword && (
              <p className="text-xs text-red-500">{errors.confirmPassword}</p>
            )}
          </div>

          {/* SUBMIT BUTTON */}
          <Button type="submit" disabled={isLoading}>
            {isLoading ? "Creating account..." : "Sign Up"}
          </Button>
        </div>

        <div className="text-center text-sm">
          Already have an account?{" "}
          <a href="/login" className="underline text-primary">
            Log in
          </a>
        </div>
      </form>
    </AuthLayout>
  )
}

export default SignUp