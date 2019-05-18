import re

weather_file = open(r'Z:\Private\nabm\python\intro_to_python_course\fundamentals\m4_files\world_temp_mean.txt', 'a+')
weather_file.write('Rio de Janeiro,Brazil,30.0,18.0')
weather_file.seek(0,0)

headings = weather_file.readline().strip()
headings_list = headings.split(",")
city_temp = weather_file.read()
city_temp_list = re.split(',|\n', city_temp)        # using re module for multiple delimiters for .split() method.

weather_file.close()

print(headings_list)
print(city_temp_list)

index = 0

while index <= len(city_temp_list)-1:
    city_name = city_temp_list[index]
    high_temp = city_temp_list[index + 2]
    print(headings_list[0].title(), "of", city_name, headings_list[2], "is", high_temp)
    index += 4

