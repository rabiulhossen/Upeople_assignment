def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
        



# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'




# 3

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag



# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

print(any_lowercase4("Hello"))
# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True