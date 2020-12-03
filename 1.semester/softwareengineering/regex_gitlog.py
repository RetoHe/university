import re
import csv

results = []
with open("gitlog.txt") as file:
    with open('Ü3.csv', mode='w') as gitlog_file:
        writer = csv.writer(gitlog_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Commit-Hash", "Timestamp", "Author", "Author Email", "Subject"])
        for line in file:
            match = re.search("(\w+) (\d+) <(\w+ \w+)>\s*\<(.*?)\>\s*\<(.*?)\>", line)

        if match:
            writer.writerow([match.group(1), match.group(2), match.group(3), match.group(4), match.group(5)])
