def laptop(turns_on,internet_works,is_slow):
  if turns_on == "no":
    return "Restart it"
  elif internet_works == "no":
    return "Airplane Mode"
  elif is_slow == "yes":
    return "Let it start properly"
  else:
    return "No problem"
turns_on = input("Yes/No ")
internet_works = input("Yes/No ")
is_slow = input("Yes/No ")

print(laptop(turns_on,internet_works,is_slow))
