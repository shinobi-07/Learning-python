height=int(input("what is your height:"))
credits=int(input("how manyy credits do you have:"))
if height >=137 and credits >=10:
  print("enjoy the ride")
elif credits>=10 and height < 137:
  print ("you're not tal enough to ride")
elif height >= 137 and credits <10: 
  print ("you don't have enough credits")
else :
  print("you've not met either requirement")      
