import re
match = re.match('Hello[ \t](.*)world', 'Hello python world')
print(match.group(1))
print(match.groups())

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())

print(re.split('[/:]', '/usr/home/lumberjack'))