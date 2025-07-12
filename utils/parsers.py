from difflib import get_close_matches

VALID_COMMANDS = [
    "add contact", "edit contact", "delete contact", "find contact", "show birthdays",
    "add note", "edit note", "delete note", "find note", "find by tag",
    "help", "save", "exit"
]

def suggest_command(user_input: str) -> str | None:
    user_input = user_input.strip().lower()
    matches = get_close_matches(user_input, VALID_COMMANDS, n=1, cutoff=0.6)
    return matches[0] if matches else None
