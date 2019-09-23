# Part 1
## download the file and use the command line change the directory to "handson/"
```
yg336@corellia:~$ wget https://raw.githubusercontent.com/igorsteinmacher/INF502-Fall2019/master/assignments/handson.zip
yg336@corellia:~$ unzip handson -d ./handson
yg336@corellia:~$ cd handson/handson
```

## 1.Draw a diagram of the commits and branches in repository
```
yg336@corellia:~/handson/handson$ git branch
yg336@corellia:~/handson/handson$ git checkout math
yg336@corellia:~/handson/handson$ git log --decorate
yg336@corellia:~/handson/handson$ git checkout master
yg336@corellia:~/handson/handson$ git log --decorate
```
![diagram](/res/git_graph.png)

## 2.Try git log --graph --all to see the commit tree. What do you see?
```
It shows the changes in ASCII graph. We can clearly see that when the repository is established, when the new branch is made and all commits and conflicts.
```

## 3.Use git diff BRANCH_NAME to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.
```
yg336@corellia:~/handson/handson$ git diff math
This operation will compare the file with same name in master with the file in math. The diffenences are shown with a start of + and -. + means the line is only in the file of current branch. - means the line is only in the file of compared branch.
```

## 4.Write a command sequence to merge the non-master branch into master
```
yg336@corellia:~/handson/handson$ git checkout master
yg336@corellia:~/handson/handson$ git merge math

```

## 5.Write a command (or sequence) to (i) create a new branch called math (from the master) and (ii) change to this branch
```
yg336@corellia:~/handson/handson$ git branch math
yg336@corellia:~/handson/handson$ git checkout math
```

## 6.omitted

## 7.Write a command (or sequence) to commit your changes
```
yg336@corellia:~/handson/handson$ git add B.py
yg336@corellia:~/handson/handson$ git commit -m "added two lines in B.py"
```

## 8.Change back to the master branch and change B.py adding the following source code (commit your change to master):
```
yg336@corellia:~/handson/handson$ git checkout master

```

## 8.omitted

## 9.Write a command sequence to merge the math branch into master and describe what happened
```
yg336@corellia:~/handson/handson$ git merge math
**there is a conflict when merge**
```

## 10.Write a set of commands to abort the merge
```
yg336@corellia:~/handson/handson$ git merge --abort
```

## 11.Now repeat item 10, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure
```
** method 1 **
1. Since now we are in master branch, we can first abort the merge.
2. Edit B.py and delete the two lines
3. Merge again. 

** method 2 **
1. Abort the merge and checkout to the math branch. 
2. Edit B.py and delete the two lines added. 
3. Go back to master branch and merge again.

** method 3 **
1. Abort the merge and checkout to the math branch. 
2. Copy the two lines.
3. Checkout to master branch.
4. Edit B.py and paste the two lines in suitable position. 

```

## 12.Write a command (or set of commands) to proceed with the merge and make master branch up-to-date
```
yg336@corellia:~/handson/handson$ git merge math
yg336@corellia:~/handson/handson$ git merge --abort
yg336@corellia:~/handson/handson$ vim B.py
** in vim press 'd' twice and then press "ESC"+":"+"wq"**
yg336@corellia:~/handson/handson$ git add B.py
yg336@corellia:~/handson/handson$ git commit -m "delete two lines"
yg336@corellia:~/handson/handson$ git merge math -m "manual merge"
yg336@corellia:~/handson/handson$ git checkout
```

# Part 2
## 4
```
1. In the repository "igorsteinmacher / INF502-Fall2019", press "Fork" in the upper right corner to fork this repository to my account.
2. Turn to my page and enter the repositiry "YuanGao-NAU/INF502-Fall2019".
3.click "Clone or download" and copy the link listed.
3. Type "git clone [link_copied]" in the terminal and press enter.
4.Type "cd INF502-Fall2019" and press enter to enter the workspace.
5. set up a file named "Gao_Yuan.md" and edit it with vim use followed steps:
    1)vim Gao_Yuan.md
    2)press "i"
    3)enter what I am required
    4)press "ESC" + ":" + "wq"
6. Type "git add Gao_Yuan.md" then press enter.
7. Type "git commit -m "add Gao_Yuan.md""
8. Type " git remote add upstream https://github.com/igorsteinmacher/INF502-Fall2019.git" and then press enter.
9. Type "git push" to update to my own repository.
9. Go to my own repository and click the "pull request" under "Clone or download".
10. In the new page, insert some information and then click "send pull request".
```

### PS: I'm very lucky that I haven't faced a lot of problems. The only problem is that I can not find the "pull request" button in the very beginning and I solved it. I found that the MarkDown is very interesting. Maybe I can use it in taking notes.
