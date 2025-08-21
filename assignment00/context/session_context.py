from openai import SQLiteSession
import os




DB_PATH = os.environ.get("MULTI_AGENT_DB", "multi_agent_session.db")
sqlite_session = SQLiteSession("multi_agent_session", DB_PATH)

