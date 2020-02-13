#list:
students=["demmy","juan","marley","bruce","gritt","larry"]
print(students) #outputs all students names
print(students[1]) #outputs second name
print(students[2]) #outputs third name
print(students[2:5]) #outputs third to fourth name
print(students[3]) #outputs forth name
print(students[3: ]) #outputs fourth to last name on list
students[3]="mark" #changes name of student in list
print(students)
#loop through the list
for student in students:
  print(student)
if "mark" in students:
  print("mark is there")
if "harry" not in students:
  print("harry is there")
  #methods
  print(len(students)) #check length of list
  students.append("nigel") #adds after last index
  print(students)
  students.insert(2,"glory") #inserts a name into specified place on list
  print(students)
  students.pop(1) #deletes second name from list
  print(students)
  students.remove("demmy") #removes an element from list
  print(students)
  students.reverse() #reverse the order of the elements
  print(students)
  students.sort() #sorts the list in alphabetical order
  print(students)