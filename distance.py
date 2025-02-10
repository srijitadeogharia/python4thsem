
# Define the distance of the race in kilometers
distance_km = 10

# Define the total time taken for the race in minutes and seconds
total_minutes = 43
total_seconds = 30

# Convert the total time to hours
total_time_hours = (total_minutes * 60 + total_seconds) / 3600

# Convert the distance to miles (1 kilometer = 0.621371 miles)
distance_miles = distance_km * 0.621371

# Calculate the average speed in miles per hour
average_speed_mph = distance_miles / total_time_hours

# Calculate the average time per mile in minutes and seconds
average_time_per_mile_minutes = int(total_time_hours * 60 / distance_miles)
average_time_per_mile_seconds = int((total_time_hours * 3600 / distance_miles) % 60)

print(f"Average time per mile: {average_time_per_mile_minutes} minutes {average_time_per_mile_seconds} seconds")
print(f"Average speed: {average_speed_mph:.2f} miles per hour")
