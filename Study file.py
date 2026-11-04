File=open("study.txt","w")

File.write(""" Like Terms: Terms like 3x and 5x can be added together to make 8x.
 Unlike Terms: Terms like 4x and 7y cannot be combined because the variables are different.
 Constants: Numbers without variables like 6 and 11 can always be combined.
 Example: 4x + 6 + 2x - 3 simplifies directly to 6x + 3.""")

File.close()

File=open("study.txt","r")

print(File.read())

File.close()