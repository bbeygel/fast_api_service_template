import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="server:app",
                host="127.0.0.1",
                port=3000,
                log_level="info",
                env_file=".env",
                reload=True)
