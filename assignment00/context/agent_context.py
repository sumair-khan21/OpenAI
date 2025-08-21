# context/agent_context.py
# Agent-specific local context manager classes/files.

from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class LocalContext:
    """
    Lightweight local context using dataclass.
    - dataclass is simple and great for in-memory, lightweight containers.
    - NOT used for validation — for validated schemas use Pydantic.
    """
    last_user_query: str = ""
    meta: Dict[str, Any] = field(default_factory=dict)

    def update_query(self, query: str):
        self.last_user_query = query
