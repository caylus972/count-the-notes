# taking total amout as inpy from user
Amount =int(input("please enter amount for withdraw :"))
# calculating the number of notes of diffrent denominations
note_1 = Amount//100
note_2=(Amount%100)//50
note_3= ((Amount%100)%50)//10

print ("notes of 100 rupe", note_1)
print ("notes of 50 rupee",note_2)
print("notes of 10 rupee", note_3)
          
