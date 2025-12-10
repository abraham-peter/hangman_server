import uvicorn


if __name__ == "__main__": # Initializarea inceput pentru aplicatia cu app, in folderul app cu numele app (foarte inspirat Peter :))
    uvicorn.run("app.app:app",port=8000,reload=True)