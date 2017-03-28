#lists

lst1=['akarsh',"bachu",1,2,3];
#prints total list
print lst1;
#   or
for i in lst1:
    print i;
#to print member of list
print lst1[0];
lst2=['python','java'];

#i.e list inside a list
lst1.append(lst2);
print lst1,"++++";

#getting list of list into another var to access inner list members
lst3=lst1[5];
print lst3[0];

#empty list is alos possible
print []

#lists are mutable(can be changed)
lst1[1]='b';#changed bachu to b
print lst1;

#to print length of list
print "length of list is: ",len(lst1);

#for loop using range function
languages=['java','python','c#']
for i in range(len(languages)):
    print "language ",i,languages[i];

#adding two lists to form one list
a=[1,2,3];
b=[4,5,6];
c=a+b;  #[1,2,3,4,5,6]
print c;

#slicing same as in strings
print lst1[0:3],lst1[:2],lst1[3:],lst1[:];

#Other way of creating lists using list() method
lst4=list();
lst4.append('akarsh');
lst4.append('learning');
lst4.append('python');
print lst4;

#list operations

lst4.pop(0);
print "pop operation performed on index 0",lst4;

print "index of python is: ",lst4.index('python');

lst4.insert(2,'java');
print "after inserting java",lst4

lst4.remove('java')
print "after removing java",lst4

lst4.reverse();
print "reversed list: ",lst4;

lst4.sort();
print "sorted list: ",lst4;

#lst1 is added at the end of lst4
lst4.extend(lst1)
print lst4;

# in operator
print 'python' in lst4

print 'dhsavh' not in lst4

# many functions that take list as parameter:
nums=[2,1,3,5,4,6];
print "max,min of list: ",max(nums),min(nums);

print "sorted list: ",sorted(nums)

print "sum of list elements: ",sum(nums);

#Converting string to list
str="hello there"
stuff=str.split();
print stuff;

#lists on both lhs and rhs
[x,y]=[1,2];
print x,y;