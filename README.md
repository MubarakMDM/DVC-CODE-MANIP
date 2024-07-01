# DVC-CODE-MANIP

# DVC-CODE-MANIP

git init
dvc init

git remote add origin url
dvc remote add -d myremote 'path'

git add .
git commit -m "initial commit"

# execute the code (write and execute the code)

dvc add data/xyz.csv
git add .
git commit -m "first commit"

dvc push 
git push origin main/master

git status
dvc status

#change code and execute

dvc add data/xyz.csv
git add .
git commit -m "second commit"

dvc  push
git push origin master

git log 

git checkout hash_code
dvc checkout

*************to execute on a particular machine************
#clone the projet from github
dvc fetch
dvc checkout

#to change the version of code
git checkout hash_code
dvc pull OR dvc fetch then dvc checkout

