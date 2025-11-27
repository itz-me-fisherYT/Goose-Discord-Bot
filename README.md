# Discord Multi-Tool Bot  
A powerful, modular Discord bot built with **Python** and **discord.py**, featuring moderation, slash commands, reaction roles, anti-spam, economy, welcome images, backups, a dashboard, and more.

---

## 📛 Badges

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.3-purple?logo=discord)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintained](https://img.shields.io/badge/Maintained-Yes-success)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 🚀 Features

### 🔧 Core Systems
- Full **slash command** support  
- Modular **Cog** structure  
- Auto-restart script  
- Environment-based token loading (`.env`)  
- Logging of edits & deletes  

### 🔨 Moderation
- Kick / Ban / Purge commands  
- Anti-Spam protection  
- Anti-Link filtering  
- Logging to a `#logs` channel  

### 🎉 Community Tools
- Reaction Roles with **buttons**  
- Ticket system  
- Leveling system with XP + auto-level ups  
- Welcome messages with automatically generated **welcome images**  

### 💰 Economy System
- SQLite-backed  
- Commands:
  - `!bal` — check balance  
  - `!daily` — claim daily reward  
- Expandable for:
  - Shops  
  - Items  
  - Inventory  
  - Trading  

### 🗄️ Auto-Backups
- Metadata-only backups every hour  
- Stored in `/data/backups/`  
- Safe + TOS friendly  

### 🖥️ Dashboard
- Flask-based web dashboard  
- Reads backup data  
- Expandable to full moderation & economy viewer  

---

## 📁 Folder Structure

```
discord_bot/
│   main.py
│   requirements.txt
│   start.bat
│   req.bat
│   .env  (you create)
│
├── cogs/
│   ├── moderation.py
│   ├── logging_system.py
│   ├── levels.py
│   ├── welcome.py
│   ├── reaction_roles.py
│   ├── anti.py
│   ├── economy.py
│   ├── backups.py
│   └── slash.py
│
├── data/
│   ├── levels.json
│   ├── backups/
│   └── welcome/
│
└── dashboard.py
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
or on Windows:
```sh
req.bat
```

### 3️⃣ Create a `.env` File
```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4️⃣ Run the Bot
```sh
python main.py
```

Or use the auto-restart script:

```sh
start.bat
```

---

## ✔️ Requirements
- Python 3.9+  
- `discord.py`  
- `Flask`  
- `Pillow`  
- `python-dotenv`  
- `aiosqlite`

(All included in `requirements.txt`)

---

## 📜 Roadmap

### Completed:
- ✔ Slash commands  
- ✔ Dashboard skeleton  
- ✔ Anti-spam system  
- ✔ Anti-link filtering  
- ✔ Reaction roles  
- ✔ Level system  
- ✔ Welcome images  
- ✔ Auto-backups  
- ✔ Economy base  

### Planned:
- ⬜ Full dashboard control (roles, bans, tickets)  
- ⬜ Inventory/shop/trading system  
- ⬜ Music system  
- ⬜ Full web-based configuration  
- ⬜ Auto-moderation AI module  

---

## 🧩 Contributing
Pull requests are welcome!  
Feel free to open an issue for suggestions, bugs, or feature requests.

---

## 📜 License
This project is licensed under the **MIT License**.
