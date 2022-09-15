######################## f STRINGS ###############################

home = "Forfar"
away = "East Fife"
home_score, away_score = 4, 5
str_var4 = f"Final score was {home} {home_score} {away} {away_score}..."
print(str_var4)

# Final score was Forfar 4 East Fife 5...




#################### .format() method ##########################


out = "The chances of randomly guessing a 4 character password at the first attempt are {0:.8f} or {0}".format(1/(95**4))
print(out)

# The chances of randomly guessing a 4 character password at the 
# first attempt are 0.00000001 or 1.2277376631548254e-08

