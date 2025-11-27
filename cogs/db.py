import aiosqlite, os, json
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bot.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS economy (
            guild_id INTEGER,
            user_id INTEGER,
            coins INTEGER DEFAULT 0,
            PRIMARY KEY (guild_id, user_id)
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS warns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guild_id INTEGER,
            user_id INTEGER,
            moderator_id INTEGER,
            reason TEXT,
            created_at INTEGER
        )""")
        await db.commit()

async def get_db():
    return await aiosqlite.connect(DB_PATH)
