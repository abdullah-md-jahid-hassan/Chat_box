# 🗨️ Real-Time Chat Box (Django Channels)

![Project](https://img.shields.io/badge/Project-Chat%20Box-blue)
![Python](https://img.shields.io/badge/Language-Python%203.10%2B-yellow)
![Django](https://img.shields.io/badge/Framework-Django%205-green)
![Channels](https://img.shields.io/badge/Realtime-Django%20Channels-informational)
![Daphne](https://img.shields.io/badge/ASGI-Daphne-purple)
![Redis](https://img.shields.io/badge/Channel%20Layer-Redis-red)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-orange)

A lightweight real-time chat application built with Django and Channels. It supports multi-room conversations over WebSockets, using Redis as the channel layer and Daphne as the ASGI server. The UI is a clean, responsive Bootstrap layout, and messages are broadcast to everyone in a room instantly.

---

## 🔍 Features

- 🔄 **Real-time messaging** via WebSockets
- 🏷️ **Named messages**: include sender `name` with each message
- 🗂️ **Multi-room support**: join by URL like `/name/room_name/`
- 📢 **Group broadcasting** using Channels groups
- ⚙️ **ASGI-first setup**: `ProtocolTypeRouter` with auth + allowed hosts middleware
- 📱 **Responsive UI**: Bootstrap 5 layout and smooth interactions

---

## 🛠️ Tech Stack

| Layer      | Technology                         |
|------------|-------------------------------------|
| Backend    | Python, Django 5, Django Channels   |
| ASGI       | Daphne                              |
| Realtime   | Redis (channels_redis)              |
| Frontend   | HTML5, CSS3, Bootstrap 5, JS        |
| Versioning | Git + GitHub                        |

---

## 📁 Project Structure

```
Chat_box/
├── chat/
│   ├── consumers.py           # WebSocket consumer (connect, receive, broadcast)
│   ├── routing.py             # WebSocket URL patterns (ws/<name>/<room_name>/)
│   ├── templates/
│   │   ├── index.html         # Landing page (enter name/room)
│   │   └── room.html          # Chat room UI + WebSocket client
│   ├── urls.py                # HTTP routes: "", "<name>/<room_name>/"
│   └── views.py               # index, chat_room views
├── chatbox/
│   ├── asgi.py                # ProtocolTypeRouter (http + websocket)
│   └── settings.py            # Channels + Redis config
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### 1) Prerequisites

- Python 3.10+
- Redis server (for the Channels layer)
  - Easiest (cross-platform) via Docker:
    ```bash
    docker run -p 6379:6379 redis:7-alpine
    ```
  - Or run Redis locally (Linux/Mac). On Windows, consider WSL or Docker.

### 2) Setup

```bash
# Clone
git clone <your-repo-url>
cd Chat_box

# Create & activate a virtual environment (Windows PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install django daphne channels channels_redis

# Run migrations
python manage.py migrate
```

### 3) Run the app

You can use Django's dev server or run Daphne directly.

```bash
# Option A: Django dev server (sufficient for local dev)
python manage.py runserver

# Option B: Daphne ASGI server
python -m daphne -b 0.0.0.0 -p 8000 chatbox.asgi:application
```

Open: `http://127.0.0.1:8000/`

---

## 🔌 WebSocket & HTTP Routes

- HTTP routes:
  - `GET /` → index page
  - `GET /<name>/<room_name>/` → chat room page

- WebSocket route (handled by Channels):
  - `ws://<host>/ws/<name>/<room_name>/`

The `name` and `room_name` are used to create a group channel (e.g., `chat_<room_name>`) so all clients in the same room receive messages instantly.

---

## ⚙️ Configuration Notes

- Redis host and port are configured in `chatbox/settings.py`:
  - `CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [("127.0.0.1", 6379)]`
- Development is enabled by default (`DEBUG=True`), and `ALLOWED_HOSTS` is empty. Set appropriate values for production.
- Static files (Bootstrap via CDN) are used directly in templates.

---

## 📸 Screenshots
<img width="670" height="764" alt="Screenshot 2025-08-19 150211" src="https://github.com/user-attachments/assets/ea48e76a-5ebc-4491-baab-657ea0fe8934" />
<img width="1890" height="783" alt="Screenshot 2025-08-19 150158" src="https://github.com/user-attachments/assets/a4c30d57-7e07-432b-9974-e2773f5f0188" />



---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 👤 Author

**Abdullah Md Jahid Hassan**  
GitHub: `abdullah-md-jahid-hassan`


