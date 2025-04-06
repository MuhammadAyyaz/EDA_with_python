# def chapo(n):
#     return n
# a = "this is my own print function"
# chapo(a)
a_list = ["ayyaz", "orhan", "ayyaz", "hamdan" , "ayyaz", "ayzal", "orhan", "ayzal"]


def rem_dup(n):
    rem_1 = []
    remov = []
    for i in n:
        if i not in rem_1:
            rem_1.append(i)
        elif n.count(i) > 1:
            remov.append(i)
        else:
            rem_1.append(i)
                  
    print(f'removed {len(remov)}  duplicates and this is the set list {rem_1}')

rem_dup(a_list)