if __name__ == '__main__':
        birthdays = {
            'bob' : '28/2/1006' , 
            'siya' : '31/4/2000' ,
            'salim': '31/8/5004' ,            
            'joker' : '31/2/2020' ,
            'sarah' : '20/2/2004' , 
            'George' : '31/9/3024' }
print("This is a birthday dictionary . We have the birthdays of: ")
for name in birthdays :
        print(name)

name = input("Enter the name whose birthdate is what you are willing to see: ")

if name in birthdays:
    print("{}\'s birthday is on {}. ".format(name , birthdays[name])) 
else:
    print("oops! we don\'t have {}\'s birthdate . sorry !" .format(name))
