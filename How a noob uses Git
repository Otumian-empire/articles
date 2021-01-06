Title
Introduction to Git - Noobs Git

Introduction
Lets see if I can make you believe in git and use git in your daily developement activities.

Git is a small software that is used to keep track of files that make up our softwares. Git with Github enables multiple developers to remotely work on a software. Do you need a reason to use git? I mean do you need a reason to keep track of the files you are working on? [why-use-git]?. If it is confusing, stop reading and get back here.

Before anything, I would be happy if I assume you are here because you want to learn a bit or nickle about Git. First you need an account from [Github]. Create an account if you do not have one else create an account. Login in if you already have an account.

We will be using a text file to simple demonstrate how to use Git.

INSTALL GIT
Lets install git on our local machines, from [git-scm].

nix: https://git-scm.com/download/linux
win: https://git-scm.com/download/win
mac: https://git-scm.com/download/mac

Open your terminal/command line/Shell. I will be saying terminal from henceforth. Type, git --version and hit enter. [LOGO git-version]

My current version is 2.29.2, yours may be higher.

BASIC WORK FLOW

Initialize (start) git
Lets create a folder on our Desktop, git-game then initialize git with the command, git init. How you create your folder is up to you. I will use the terminal. [LOGO create-dir-and-init-git]

I navigated to my Desktop, created a folder called git-game. Changed directory into git-game then i initiliazed git.

You can open the folder with a text editor of your choice.


GIT CONFIG
Set your default username and email with,
git config --global user.name <your-username>
git config --global user.email <your-email>


Set your local (specific to project) username and email with,
git config --global user.name <your-username>
git config --global user.email <your-email>

Usually, your email and username will match your github email and username.

Create file
Lets create a single text file called index.txt and add about two lines of text.
I will add, "Hello there" and "I am learning git" as the two lines.

Note that index.txt is to be created inside the folder, git-game.



Add file
The new file we justed created, index.txt is untracked by git. enter git status in the terminal. {LOGO git-status].
What git status does is to display the status of all the file in the git-game directory in our case. This may look difference in vscode, as U will be displayed beside the file. U means untracked.

To track the file or let git know of the presence of a file, you do, git add filename. In our case git add index.txt. Now another git status will show a different result. [LOGO git-add-status].

If you noticed, it said something like on branch master. Now it is not supposed to be master but main. We have to fix this before we move forward. Refer to how to [change-branch-name-from-master-to-main] if you get confused.

So in git-game, after we issued the git init command, a hidden folder was created, called .git. Inside .git there is a file, HEAD. Edit HEAD and change master to main. I will do this on on the terminal. As vim ./git/HEAD (Vim is a text editor - use your favourite text editor or notepad) [LOGO master-branch]

After the update is done, our git status should look more or less like, it is in the image below.
[LOGO mian-branch]

Yu have to rename the branch name every time you git init or as far as the default branch is master.



Commit
Modify index.txt and do a git status. You'd see that index.txt has been modified. [LOGO update-git-status]
Now, before we can commit, lets add the new changes with a git add index.txt [LOGO git-add-status-2]

A commit is like a who zipped or compressed version of your project directory and all it files that have been add to git. So after a git commit you would have an version of your application sitting rather on your local repository. 

Now lets commit, git commit -m "<message>", <message> is a descriptive text you pass when making a commit. This should be referencial as it kind of summarizes what that commit/compression is all about.

I have only two lines in index.txt so may be I would say, git commit -m "index.txt has only two lines".
[LOGO git-commit]

Say, if we want to add another file, README.md. We would have to add then commit.


create remote repository, add locally
Lets create remote repository on github

Push to github








Body

Source
[git-scm]:https://git-scm.com/
[github]:https://github.com/
[why-use-git]:https://miguelgfierro.com/blog/2017/10-reasons-why-you-should-be-using-git-in-software-projects/
[change-branch-name-from-master-to-main]:https://dev.to/otumianempire/change-branch-name-from-master-to-main-50ei
Conclusion+question
