"""
Basic usage examples for the Tabroom API client.
"""

from tabroom import TabroomClient, TabroomError

# Option 1: Initialize with credentials (auto-login)
client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)
print(f"Authenticated: {client.is_authenticated()}")
print(f"Token: {client.token}")

# Option 2: Initialize with existing token (no login needed)
client = TabroomClient(token="your_existing_token")

# Option 3: Initialize without credentials, login later
client = TabroomClient()
client.login("your_email@example.com", "your_password")

# Option 4: Use as a context manager (automatically closes connection)
with TabroomClient(username="your_email@example.com", password="your_password") as client:
    try:
        # Get your user profile
        profile = client.user.get_profile()
        print(f"Logged in as: {profile.first} {profile.last}")
        print(f"Email: {profile.email}")

        # Search for upcoming tournaments
        tournaments = client.public.search_tournaments(
            time="future",
            search_string="TOC"
        )
        print(f"\nFound {len(tournaments)} tournaments")

        # Get upcoming tournaments
        upcoming = client.public.get_upcoming_tournaments()
        for tournament in upcoming:
            if tournament.name:
                print(f"- {tournament.name}")

        # Get a specific tournament by ID
        tournament = client.public.get_tournament_by_id(12345)
        print(f"\nTournament: {tournament.name}")

        # Check system status
        status = client.system.get_status()
        print(f"\nAPI Status: {status}")

    except TabroomError as e:
        print(f"Error: {e.message}")
        if e.status_code:
            print(f"Status code: {e.status_code}")
