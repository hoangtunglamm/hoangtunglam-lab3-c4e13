def get_even_list(l):

    for i in l :
        if i % 2 != 0 :
            l.remove(i)

    return l

l =[1, 2, 5, -10, 9, 6, -1, -31,-33,-35,-3]
even_list = get_even_list(l)
print(even_list)


# if set(even_list) == set([2, -10, 6]):
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")

#không hiểu sao cho thêm mấy số âm vào thì sai :|
