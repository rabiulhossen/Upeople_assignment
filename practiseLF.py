"""
def check(n):
    while n !=1:
        print(n)
        if n%2:
            n = n/2
            break
        else:
            n=n+3
      

print(check(12))
        
while True:
 line = input('> ')
 if line == 'done':
  break
print(line)
print('Done!')

"""



name ="Rabiul Hossen"
print("MY name is:", name)
# Display n characters from left
n = int(input("Enter the number of characters to display from left: "))
print("Left", n, "characters:", name[:n])


# Count the number of vowels
vowels = "AEIOUaeiou"
count = 0
for char in name:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

4


# Reverse the name
reverse_name = name[::-1]
print("Reversed name:", reverse_name)
4