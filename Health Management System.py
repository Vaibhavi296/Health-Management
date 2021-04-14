import datetime
def gettime():
    return datetime.datetime.now()

lock_retrieve=int(input("Enter 1 for lock and 2 for retrieve:"))
name=int(input("Enter 1 for Kushal,2 for Vaibhavi,3 for Nishka:"))
diet_exer=int(input("Enter 1 for diet and 2 for Exercise:"))

if lock_retrieve==1:
    if name==1:
        if diet_exer==1:
            Kushal_diet=input("enter the diet:")
            with open("Kushal Diet.txt",'a') as f:
              f.write(str([str(gettime())])+ ":" +Kushal_diet+"\n")
        else:
              Kushal_exercise=input("Enter the exercise:")
              with open("Kushal Exercise",'a') as f:
                  f.write(str([str(gettime())])+":"+Kushal_exercise+"\n")
    elif name==2:
        if diet_exer==1:
            Vaibhavi_diet=input("enter the diet:")
            with open("Vaibhavi Diet.txt",'a') as f:
              f.write(str([str(gettime())])+ ":" +Vaibhavi_diet+"\n")
        else:
              Vaibhavi_exercise = input("Enter the exercise:")
              with open("Vaibhavi Exercise", 'a') as f:
                  f.write(str([str(gettime())]) + ":" + Vaibhavi_exercise + "\n")
    else:
        if diet_exer==1:
            Nishka_diet=input("enter the diet:")
            with open("Nishka Diet.txt",'a') as f:
              f.write(str([str(gettime())])+ ":" +Nishka_diet+"\n")
        else:
              Nishka_exercise = input("Enter the exercise:")
              with open("Nishka Exercise", 'a') as f:
                  f.write(str([str(gettime())]) + ":" + Nishka_exercise + "\n")
elif lock_retrieve==2:
    if name==1:
        if diet_exer==1:
            with open("Kushal Diet.txt") as f:
                 for i in f:
                     print(i,end="")

        else:

              with open("Kushal Exercise") as f:
                 for i in f:
                     print(i, end="")
    elif name==2:
        if diet_exer==1:

            with open("Vaibhavi Diet.txt") as f:
              for i in f:
                  for i in f:
                      print(i, end="")

        else:

              with open("Vaibhavi Exercise") as f:
                  for i in f:
                      print(i, end="")
    else:
        if diet_exer==1:

            with open("Nishka Diet.txt") as f:
                for i in f:
                    print(i, end="")
        else:

              with open("Nishka Exercise") as f:
                  for i in f:
                      print(i, end="")
