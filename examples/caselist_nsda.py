"""
Examples for caselist and NSDA integration.
"""

from tabroom import TabroomClient

client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)

PERSON_ID = 12345

# Caselist operations
print("=== Caselist ===")

# Get students
students = client.caselist.get_students(PERSON_ID)
print(f"Found {len(students)} students")
for student in students:
    print(f"- {student.name}")

# Get rounds
rounds = client.caselist.get_rounds(PERSON_ID)
print(f"\nFound {len(rounds)} rounds")

# Get chapters
chapters = client.caselist.get_chapters(PERSON_ID)
print(f"Found {len(chapters)} chapters")

# Create a caselist link
link_data = {
    "url": "https://caselist.example.com/team/123",
    "description": "Team caselist"
}
link = client.caselist.create_link(link_data)
print(f"\nCreated caselist link: {link.url}")

# NSDA operations
print("\n=== NSDA ===")

NSDA_ID = 54321

# Get NSDA history
history = client.nsda.get_history(NSDA_ID)
print(f"NSDA History: {history}")

client.close()
