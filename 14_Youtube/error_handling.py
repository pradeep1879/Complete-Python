file = open('youtube.txt', 'w')

try:
    file.write('hi there')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('hi there')