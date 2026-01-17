import { useState } from "react"

function Sidebar() {
  const [currentPath, setCurrentPath] = useState("/dashboard")
  
  // Menu items
  const menuItems = [
    { 
      name: "Dashboard", 
      path: "/dashboard",
      icon: "🏠" // Replace with actual icons later
    },
    { 
      name: "Items", 
      path: "/items",
      icon: "💼"
    },
    { 
      name: "Admin", 
      path: "/admin",
      icon: "👥"
    }
  ]

  return (
    <aside className="w-64 border-r border-sidebar-border bg-sidebar flex flex-col h-screen fixed inset-y-0 left-0 z-30">
      {/* LOGO SECTION */}
      <div className="h-16 flex items-center px-6 border-b border-sidebar-border">
        <span className="font-bold text-lg text-sidebar-primary-foreground bg-sidebar-primary px-3 py-1 rounded">
          MyApp
        </span>
      </div>

      {/* NAVIGATION MENU */}
      <nav className="flex-1 overflow-y-auto p-4 space-y-2">
        {menuItems.map((item) => (
          <a
            key={item.path}
            href={item.path}
            onClick={(e) => {
              e.preventDefault()
              setCurrentPath(item.path)
              window.location.href = item.path
            }}
            className={`flex items-center gap-3 px-3 py-2 text-sm font-medium rounded-md transition-colors ${
              currentPath === item.path
                ? "bg-sidebar-accent text-sidebar-accent-foreground"
                : "text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
            }`}
          >
            <span className="text-xl">{item.icon}</span>
            {item.name}
          </a>
        ))}
      </nav>

      {/* USER PROFILE SECTION (Bottom) */}
      <div className="border-t border-sidebar-border p-4">
        <div className="flex items-center gap-3 px-2">
          <div className="h-8 w-8 rounded-full bg-sidebar-primary flex items-center justify-center text-sidebar-primary-foreground font-semibold">
            A
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-sm font-medium text-sidebar-foreground truncate">
              Admin User
            </p>
            <p className="text-xs text-sidebar-foreground/70 truncate">
              admin@example.com
            </p>
          </div>
          <button className="text-sidebar-foreground/70 hover:text-sidebar-foreground">
            ⚙️
          </button>
        </div>
      </div>
    </aside>
  )
}

export { Sidebar }