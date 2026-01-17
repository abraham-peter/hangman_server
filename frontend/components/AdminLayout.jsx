import { Sidebar } from "./Sidebar"
function AdminLayout({ children }) {
  return (
    <div className="flex min-h-screen w-full bg-background">
      {/* SIDEBAR - Fixed on the left */}
      <Sidebar />
      
      {/* MAIN CONTENT - Takes up remaining space */}
      <div className="flex flex-1 flex-col pl-64">
        {/* Header */}
        <header className="sticky top-0 z-10 flex h-16 shrink-0 items-center gap-2 border-b bg-background px-4">
          <h2 className="text-lg font-semibold">Admin Panel</h2>
        </header>

        {/* Page Content */}
        <main className="flex-1 p-6 md:p-8">
          <div className="mx-auto max-w-7xl">
            {children}
          </div>
        </main>
      </div>
    </div>
  )
}

export { AdminLayout }