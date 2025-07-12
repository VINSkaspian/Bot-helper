from datetime import datetime

class Note:
    def __init__(self, text, tags=None):
        self.text = text
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tags = tags if tags else []

    def __str__(self):
        tags_str = ", ".join(self.tags) if self.tags else "без тегів"
        return f"[{self.created}] {self.text} (теги: {tags_str})"
