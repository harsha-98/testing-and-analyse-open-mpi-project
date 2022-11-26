from datetime import datetime

from pydriller import Repository

commitDict = {}
dateDict = {}
authorDict = {}
i = 0

for commit in Repository('https://github.com/open-mpi/ompi', filepath='test').traverse_commits():
    print("date loop")
    for m in commit.modified_files:
        if m.filename not in dateDict:
            dateDict[m.filename] = commit.author_date

for commit in Repository('https://github.com/open-mpi/ompi', filepath='test', since=datetime(2020, 1, 5, 17, 0, 0)).traverse_commits():
    print("enter")

    if commit.author.name in authorDict:
        authorDict[commit.author.name] = authorDict[commit.author.name] + 1
    else:
        authorDict[commit.author.name] = 1

    for m in commit.modified_files:
        if m.filename in commitDict:
            commitDict[m.filename] = commitDict[m.filename] + 1
        else:
            commitDict[m.filename] = 1

    i = i + 1

    print(i)

with open("commitCountPerFile.txt", 'w') as f:
    for key, value in commitDict.items():
        f.write('%s , %s\n' % (key, value))

with open("commitDates.txt", 'w') as f:
    for key, value in dateDict.items():
        f.write('%s , %s\n' % (key, value))

with open("authorContribution.txt", 'w') as f:
    for key, value in authorDict.items():
        f.write('%s , %s\n' % (key, value))
