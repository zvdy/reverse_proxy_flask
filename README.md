# Flask Reverse Proxy to Backend Server

This is a simple Flask app that acts as a reverse proxy to a backend server. It is intended to be used as a base for other Flask apps that need to proxy to a backend server.

## Usage
```
git clone https://github.com/zvdy/reverse_proxy_flask.git

cd reverse_proxy_flask

```

> Note: I recommend ussing Live server extension for VS Code to run the frontend, once the frontend is running you can run the backend server and reverse proxy server in different terminals.

```
# Run the frontend using Live Server extension

---

# Terminal 1
# Run the backend
cd backend
python3 main.py

---

# Terminal 2
# Run the reverse proxy
cd reverse_proxy
python3 main.py
```

## License
[MIT License](LICENSE)
