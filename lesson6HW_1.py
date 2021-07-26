name = ['abc','def','ghi','jkl']
score = [10,90,100,85]
i = 0
max = 0
while i < 4:
   print(name[i],score[i])
   
   if score[i] > max:
        max = score[i]
   else:
      max = max
   i = i + 1

print (max)