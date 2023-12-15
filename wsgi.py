from server import app

if __name__ == "__main__":
    SERVER_PORT = os.environ.get("SERVER_PORT", "8080")
    app.run(host="", port=int(SERVER_PORT))
