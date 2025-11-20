"""
Examples of error handling with the Tabroom API client.
"""

from tabroom import (
    TabroomClient,
    TabroomError,
    TabroomAuthError,
    TabroomNotFoundError,
    TabroomValidationError,
    TabroomServerError,
)

client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)

# Handle specific error types
try:
    # This will fail if credentials are wrong
    profile = client.user.get_profile()
    print(f"Logged in as: {profile.first} {profile.last}")

except TabroomAuthError as e:
    print(f"Authentication failed: {e.message}")
    print("Please check your credentials")

except TabroomError as e:
    print(f"API error: {e.message}")


# Handle not found errors
try:
    # Try to get a tournament that doesn't exist
    tournament = client.public.get_tournament_by_id(999999999)

except TabroomNotFoundError as e:
    print(f"Tournament not found: {e.message}")

except TabroomError as e:
    print(f"API error: {e.message}")


# Handle validation errors
try:
    # This might fail with validation error if data is invalid
    result = client.access.tournament(123).grant(456, {"invalid": "data"})

except TabroomValidationError as e:
    print(f"Validation error: {e.message}")
    print("Please check the data format")

except TabroomError as e:
    print(f"API error: {e.message}")


# Handle server errors
try:
    # Server might be down or having issues
    status = client.system.get_status()

except TabroomServerError as e:
    print(f"Server error: {e.message}")
    print("The API server might be experiencing issues")

except TabroomError as e:
    print(f"API error: {e.message}")


# Generic error handling
try:
    tournaments = client.public.search_tournaments("future", "TOC")

except TabroomError as e:
    print(f"Error: {e.message}")
    if e.status_code:
        print(f"HTTP Status: {e.status_code}")

finally:
    client.close()
