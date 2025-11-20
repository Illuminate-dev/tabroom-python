"""
Examples for managing access control and permissions.
"""

from tabroom import TabroomClient

client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)

TOURN_ID = 12345
PERSON_ID = 789

# Grant tournament-level access
permissions = {
    "level": "admin",
    "can_edit": True
}
client.access.tournament(TOURN_ID).grant(PERSON_ID, permissions)
print(f"Granted tournament access to person {PERSON_ID}")

# Grant event-level access
EVENT_ID = 456
event_permissions = {
    "level": "staff",
    "can_tab": True
}
client.access.tournament(TOURN_ID).event(EVENT_ID).grant(PERSON_ID, event_permissions)
print(f"Granted event access to person {PERSON_ID}")

# Grant category-level access
CATEGORY_ID = 101
category_permissions = {
    "level": "viewer",
    "can_view": True
}
client.access.tournament(TOURN_ID).category(CATEGORY_ID).grant(PERSON_ID, category_permissions)
print(f"Granted category access to person {PERSON_ID}")

# Revoke access
client.access.tournament(TOURN_ID).event(EVENT_ID).revoke(PERSON_ID)
print(f"Revoked event access from person {PERSON_ID}")

client.close()
