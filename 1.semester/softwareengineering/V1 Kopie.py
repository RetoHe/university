import re

results = []
with open("battery_data.txt") as file:
    for line in file:
        match = re.search("\+(\d+)?h?(\d{2})?m?(\d{2})?s?(\d{3})ms \(\d\) (\d{3})", line)

        if match:
            result_item = [0, int(match.group(5))]
            ms = int(match.group(4))

            if match.group(2) == None and match.group(3) == None:
                result_item[0] += int(match.group(1)) * 1000
            elif match.group(2) == None:
                result_item[0] += int(match.group(1)) * 1000 * 60
                result_item[0] += int(match.group(3)) * 1000
            else:
                result_item[0] += int(match.group(1)) * 1000 * 60 * 60
                result_item[0] += int(match.group(2)) * 1000 * 60
                result_item[0] += int(match.group(3)) * 1000

            results.append(result_item)

print(results)
#\+\d{3}ms

#\d = [0-9]
#\+(\d+)?h?(\d{2})?m?(\d{2})?s?(\d{3})ms
#gro

#Für Übung mit Git Repo

#for result_item in results:
    #line = ""
    #for column in result_item:
        #line.append(str(column))
    #print(";",join(line))