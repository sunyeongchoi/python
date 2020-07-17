idx = [1, 2, 3, 4]
name = ['hong kildong', 'lee soonsin', 'jang youngsil', 'king sejong']
email = ['hong@mail.com', 'lee@mail.com', 'jang@mail.com', 'king@mail.com']
hp_num = ['010-2343-9870', '010-3333-5555', '010-7777-1234', '010-4567-0987']


my_dict = dict()
my_list = []
for i in range(len(idx)):
    my_dict['id'] = idx[i]
    my_dict['name'] = name[i]
    my_dict['email'] = email[i]
    my_dict['hp_num'] = hp_num[i]
    my_list.append(my_dict)
    print(my_list)

