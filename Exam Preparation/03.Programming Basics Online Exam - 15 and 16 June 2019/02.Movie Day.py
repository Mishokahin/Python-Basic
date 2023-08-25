shooting_time = int(input())
scenes_count = int(input())
time_per_scene = int(input())

needed_time = (scenes_count * time_per_scene) + (shooting_time * 0.15)
time_left = round(abs(shooting_time - needed_time))

print(f"You managed to finish the movie on time! You have {time_left} minutes left!" if needed_time <= shooting_time
      else f"Time is up! To complete the movie you need {time_left} minutes.")