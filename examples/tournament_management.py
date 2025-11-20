"""
Examples for tournament tabulation and management.
"""

from tabroom import TabroomClient

client = TabroomClient(
    username="your_email@example.com",
    password="your_password"
)

# Tournament ID
TOURN_ID = 12345

# Get tournament dashboard
dashboard = client.tab.tournament(TOURN_ID).get_dashboard()
print(f"Tournament Dashboard: {dashboard}")

# Get attendance for the entire tournament
attendance = client.tab.tournament(TOURN_ID).get_attendance()
print(f"Overall Attendance: {attendance}")

# Mark someone as present
client.tab.tournament(TOURN_ID).mark_attendance({
    "person_id": 789,
    "present": True
})

# Work with a specific round
ROUND_ID = 456
round_dashboard = client.tab.tournament(TOURN_ID).round(ROUND_ID).get_dashboard()
print(f"Round Dashboard: {round_dashboard}")

# Get attendance for a specific round
round_attendance = client.tab.tournament(TOURN_ID).round(ROUND_ID).get_attendance()
print(f"Round Attendance: {round_attendance}")

# Work with timeslots
TIMESLOT_ID = 789
timeslot_dashboard = client.tab.tournament(TOURN_ID).timeslot(TIMESLOT_ID).get_dashboard()
print(f"Timeslot Dashboard: {timeslot_dashboard}")

# Get judge checkin for a category
CATEGORY_ID = 101
checkin = client.tab.tournament(TOURN_ID).get_category_checkin(CATEGORY_ID)
print(f"Judge Checkin: {checkin}")

client.close()
