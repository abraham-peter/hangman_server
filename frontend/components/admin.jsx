import { useState, useEffect } from "react"
import { AdminLayout } from "../components/AdminLayout"
import { Button } from "../components/Button"

function Admin() {
  const [users, setUsers] = useState([])
  const [isLoading, setIsLoading] = useState(true)

  // FETCH USERS from API
  useEffect(() => {
    fetchUsers()
  }, [])

  const fetchUsers = async () => {
    try {
      // TODO: Replace with your actual API endpoint
      const response = await fetch("/api/users", {
        headers: {
          "Authorization": `Bearer ${localStorage.getItem("authToken")}`
        }
      })
      
      if (response.ok) {
        const data = await response.json()
        setUsers(data.data || [])
      }
    } catch (error) {
      console.error("Failed to fetch users:", error)
    } finally {
      setIsLoading(false)
    }
  }

  // MOCK DATA (for testing without backend)
  const mockUsers = [
    { 
      id: 1, 
      full_name: "Alice Smith", 
      email: "alice@example.com", 
      is_active: true, 
      is_superuser: true 
    },
    { 
      id: 2, 
      full_name: "Bob Johnson", 
      email: "bob@example.com", 
      is_active: true, 
      is_superuser: false 
    },
    { 
      id: 3, 
      full_name: "Charlie Brown", 
      email: "charlie@example.com", 
      is_active: false, 
      is_superuser: false 
    }
  ]

  // Use mock data if no real users loaded
  const displayUsers = users.length > 0 ? users : mockUsers

  return (
    <AdminLayout>
      <div className="flex flex-col gap-6">
        {/* HEADER SECTION */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold tracking-tight">Users</h1>
            <p className="text-muted-foreground">
              Manage user accounts and permissions
            </p>
          </div>
          <Button onClick={() => alert("Add user clicked!")}>
            ➕ Add User
          </Button>
        </div>

        {/* USERS TABLE */}
        <div className="border rounded-md overflow-hidden">
          <table className="w-full caption-bottom text-sm">
            <thead className="bg-muted/50">
              <tr className="border-b">
                <th className="h-10 px-4 text-left align-middle font-medium text-muted-foreground">
                  Full Name
                </th>
                <th className="h-10 px-4 text-left align-middle font-medium text-muted-foreground">
                  Email
                </th>
                <th className="h-10 px-4 text-left align-middle font-medium text-muted-foreground">
                  Role
                </th>
                <th className="h-10 px-4 text-left align-middle font-medium text-muted-foreground">
                  Status
                </th>
                <th className="h-10 px-4 text-left align-middle font-medium text-muted-foreground">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {isLoading ? (
                <tr>
                  <td colSpan="5" className="h-32 text-center text-muted-foreground">
                    Loading...
                  </td>
                </tr>
              ) : displayUsers.length > 0 ? (
                displayUsers.map((user) => (
                  <tr key={user.id} className="border-b hover:bg-muted/50 transition-colors">
                    <td className="p-4 align-middle">{user.full_name}</td>
                    <td className="p-4 align-middle">{user.email}</td>
                    <td className="p-4 align-middle">
                      <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                        user.is_superuser 
                          ? "bg-purple-100 text-purple-700" 
                          : "bg-gray-100 text-gray-700"
                      }`}>
                        {user.is_superuser ? "Superuser" : "User"}
                      </span>
                    </td>
                    <td className="p-4 align-middle">
                      <span className="flex items-center gap-2">
                        <span className={`h-2 w-2 rounded-full ${
                          user.is_active ? "bg-green-500" : "bg-red-500"
                        }`}></span>
                        {user.is_active ? "Active" : "Inactive"}
                      </span>
                    </td>
                    <td className="p-4 align-middle">
                      <button 
                        onClick={() => alert(`Edit user: ${user.full_name}`)}
                        className="text-primary hover:underline text-sm"
                      >
                        Edit
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" className="h-32 text-center text-muted-foreground">
                    No users found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </AdminLayout>
  )
}

export default Admin