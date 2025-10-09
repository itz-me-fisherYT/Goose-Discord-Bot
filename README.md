Perfect 😎 — here’s a **complete, professional, and eye-catching README.md** ready for GitHub.
It includes badges, descriptions, setup, usage, credits, and visuals — everything a polished project page should have.

You can copy-paste this straight into a file called `README.md` in VS Code.

---

````markdown
# 🎯 Discord Quote & YouTube Notification Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Discord](https://img.shields.io/badge/Discord-Bot-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![Made With](https://img.shields.io/badge/Made%20With-Love-red)

> A powerful yet easy-to-use **Discord bot** that mixes **fun quote commands**, **moderation tools**, and **automatic YouTube notifications** for videos, shorts, and live streams — all in one package!  
> Ideal for Minecraft communities, creators, or servers that love both fun and functionality.

---

## ✨ Features

### 🎭 Quote System
Keep your server inspired or entertained:
- `!quote` → Sends a random quote from your file.  
- `!addquote [text]` → Adds a new quote (Mods only).  
- `!listquotes` → Lists all quotes in a stylish Discord embed (Mods only).  

### 🛠️ Moderation Commands
Stay in control of your server with simple commands:
- `!kick @user [reason]` → Kick a user.  
- `!ban @user [reason]` → Ban a user.  
- `!clear [number]` → Delete recent messages quickly.  

### 📜 Help Command
- `!help` → Shows all commands in a clean, easy-to-read embed.

### 🎬 YouTube Notifications
Automatically checks a YouTube channel every 5 minutes and sends notifications when:
- 🟢 A **video** is uploaded → pings `@videos`  
- 🔴 A **short** is uploaded → pings `@shorts`  
- 🟣 A **stream** goes live → pings `@streams`  

> No YouTube API key required — the bot uses public RSS feeds.

### 🧪 Test Command
- `!testnotify` → Simulate pings for videos, shorts, and streams without uploading anything!

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/discord-yt-bot.git
cd discord-yt-bot
````

### 2️⃣ Install Dependencies

```bash
pip install discord.py feedparser
```

### 3️⃣ Configure the Bot

Open `bot.py` and update these values:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
DISCORD_CHANNEL_ID = 123456789012345678  # Channel ID for notifications
ROLE_STREAMS = "<@&STREAMS_ROLE_ID>"
ROLE_VIDEOS = "<@&VIDEOS_ROLE_ID>"
ROLE_SHORTS = "<@&SHORTS_ROLE_ID>"
YOUTUBE_CHANNEL_ID = "UCxxxxxxxxxxxx"  # Channel to track
```

### 4️⃣ Add a `quotes.txt` File

Create a file named `quotes.txt` in the same folder and add some quotes:

```
Be yourself; everyone else is already taken.
The best way to predict the future is to create it.
Life’s too short to wait.
```

### 5️⃣ Run the Bot

```bash
python bot.py
```

---

## 🧰 Commands Overview

| Command                | Description          | Permission      |
| ---------------------- | -------------------- | --------------- |
| `!quote`               | Sends a random quote | Everyone        |
| `!addquote [text]`     | Adds a new quote     | Manage Messages |
| `!listquotes`          | Lists all quotes     | Manage Messages |
| `!kick @user [reason]` | Kick a member        | Kick Members    |
| `!ban @user [reason]`  | Ban a member         | Ban Members     |
| `!clear [amount]`      | Clear messages       | Manage Messages |
| `!help`                | Show command list    | Everyone        |
| `!testnotify`          | Test YouTube pings   | Everyone        |

---

## 🧠 How the YouTube System Works

* The bot fetches the channel’s **RSS feed** every 5 minutes.
* If it finds a new upload:

  * The link is checked for `shorts/` → triggers a **Shorts ping**.
  * Otherwise, it triggers a **Video ping**.
* Streams are simulated using the `!testnotify` command.
* No API key needed — it’s lightweight and simple.

---

## 🧩 Example Embed

When you use `!listquotes`, your bot will send something like:

> **Quotes List**
> *"Be yourself; everyone else is already taken."*
> *"Stay hungry, stay foolish."*

Or when a new video is detected:

> 🎬 **New Video Uploaded!**
> @videos
> [https://youtu.be/example123](https://youtu.be/example123)

---

## 🖼️ Optional: Add Your Own Branding

You can easily add your own name or website in the footer of the help command:

```python
embed.set_footer(text="Created by ItzFisher.org", icon_url=ctx.author.avatar.url)
```

---

## 🧑‍💻 For Developers

* Built with **Python 3.10+**
* Uses **discord.py** and **feedparser**
* Lightweight, no external API keys required
* Ready for self-hosting or cloud hosting (Replit, Railway, etc.)

---

## ❤️ Credits

Created by **[Luke Fisher](https://discord.com/users/1319567972335091773)**
You can use this bot freely, but please give credit if you modify or share it.

---

## 📄 License

This project is licensed under the **MIT License** — you can modify and distribute freely, as long as credit is given.

---

## 🔗 Links

* 🌍 [Your Website](https://itzfisher.org)
* 💬 [Discord Profile](https://discord.com/users/1319567972335091773)
* 🧠 [GitHub Repository](https://github.com/itz-me-fisherYT/discord-yt-bot)

---

### ⭐ Like this project?

If you find it useful, consider giving it a **star** on GitHub to support future updates!

```

---

Would you like me to add a **fancy banner image** (like “Made by ItzFisher.org” or “Discord Bot”) for the top of the README too?  
That can make it look *really* professional on GitHub.
```
