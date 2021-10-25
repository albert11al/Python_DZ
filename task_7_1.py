import os


my_values = ['settings','mainapp','adminapp','authapp']
my_keys = 'my_project'
my_dict = {my_keys: my_values}
dir_path = [os.makedirs(os.path.join(my_keys, i)) for i in my_values if not os.path.exists(os.path.join(my_keys, i))]
