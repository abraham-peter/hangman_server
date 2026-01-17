function AuthLayout({ children }) {
  return (
    <div className="grid min-h-svh lg:grid-cols-2">
      {/* LEFT SIDE: Logo (hidden on mobile) */}
      <div className="bg-muted relative hidden lg:flex lg:items-center lg:justify-center">
        <div className="text-4xl font-bold">YourLogo</div>
      </div>

      {/* RIGHT SIDE: Form content */}
      <div className="flex flex-col gap-4 p-6 md:p-10">
        <div className="flex flex-1 items-center justify-center">
          <div className="w-full max-w-xs">
            {children}
          </div>
        </div>
      </div>
    </div>
  )
}

export { AuthLayout }