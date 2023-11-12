hour = int(input())
day_of_week = input()
user_output = ''

if day_of_week == "Sunday":
    user_output = 'closed'
else
    if hour >= 10 and hour <= 18:
        user_output = 'open'
    else
        user_output = 'closed'

print(user_output)



# time = int(input())
# day_of_the_week = input().lower()
#
# if day_of_the_week == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday":
#     if 10 <= time <= 18:
#         print("open")
#     else:
#         print("closed")
#
