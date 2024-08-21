print("MY LOGIN SYSTEM")
print("\n")

username = input("Username > ")
password = input("Password >")
if username == "David" and password == "hi":
  print("Why hello there David, what a lovely accent you have, you could have charmed your way in here even without a password." + "\n" + "Have a great day." + "\n" + "Don't forget to wear a hat in the sun!")
elif username == "Chad" and password == "hello":
  print("Why hello there Chad, what a lovely dog you have with you." + "\n" + "What kind of dog is that?")
elif username == "Jack" and password == "goodbye":
  print("Why hello there Jack, what a lovely cat you have with you." + "\n" + "What kind of cat is that?")
else:
  print("Invalid Entry, please try again.")
