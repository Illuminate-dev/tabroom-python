"""
Basic usage examples for the Tabroom API client.
"""

from tabroom import TabroomClient, TabroomError

# Initialize the client with credentials
client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)

# Or use as a context manager (automatically closes connection)
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
