import yaml


with open('../Data/data.yaml', 'r') as f:

    # data = yaml.load(f, Loader = yaml.FullLoader)
    # print(data)

# test: login_data01
# test_name: lili
# test_pwd: 456

# {'Test': {'login_data01': {'name': 'lili', 'pwd': 456}, \
#           'login_data02': {'name': 'nana', 'pwd': 567},\
#            'login_data03': {'name': 'haha', 'pwd': 789}}}

    data = yaml.safe_load(f).get('Test')
    print(data)
    for i in data.keys():
        print('test:%s \n test_name:%s\n test_pwd:%d'
                %(i, data.get(i).get('name'), data.get(i).get('pwd')))

