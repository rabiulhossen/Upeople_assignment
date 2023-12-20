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