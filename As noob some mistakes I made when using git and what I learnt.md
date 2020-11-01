# Some Mistakes I Made as Noob Regarding The Use of Git And What I Learnt

_So let say I am working on a feature, X_

- I worked directly from the `main` or default branch and even made commits and pushed to GitHub. This is so wrong and unacceptable, especially when I had been told to create a new branch from the `main`. The worse part was when I had admin privileges.

- Always create a new branch from the main before you touch the code.

- Pull and merge the `main` branch to the branch you are working on before you push. This will be done by the maintainer mostly when merging `featureX` to the `main` branch. So why did I say you have to pull and merge? Well, there could be some changes made to the `main` branch and such changes (merged to `featureX`) gladly reduces merge conflicts.

- Make a lot of commits, reasonable ones, as such. So for `featureX`, let sat we break the implementation into about 4 steps. Then I'd encourage you to make a commit after each phase.

- Always initialize git in the root directory of your application. You have the application developed already but you want to push it to GitHub. You then initialize git in one of the folders in the application root directory - massive dramatic human error. You then realize only part of your application exists on GitHub, magic.

- Add and always put the `.gitignore` file in the root directory of your application. Deleting unwanted files or binaries is so not awesome until you delete a file you should not have had deleted. There is the trash can but for `shift + del` guys, there is not.

- Always, at least, scan through your code before pushing. It sucks during a review, the reviewer asks you if you can not spell. This is unavoidable on it own as we type but try to. This can affect you is a fun way.

- If you messed up with a branch, a commit will save you if you have been making frequent meaningful commits. Do not delete the whole project because of a mistake on a branch and trying to clone a new copy of the project. You can just create a new branch from the `main` and start working again.

- Have a backup of your `.env` file. `.env` file paths are usually added to `.gitignore`. So when the project is deleted from your pc, there won't be a `.env` file when you clone the project again.

- I used to do `git branch featureY` from the `main` branch, then `git checkout featureY`, which could be done straight away as, `git checkout -b featureY`.

- Sometimes doing a pull after a fetch resolves a lot of conflicts. What was the simple way you solved a merge conflict?

- Git push on branch `featureZ`, `git push featureZ`, does not work since there is nowhere remotely does branch for `featureZ` exit. I had to do, `git push --set-upstream origin featureZ`. I learnt and often use, `git push origin featureZ`, and it works. Well, is there any difference between the two commands and what is it?

- Fixing merge conflict remotely (on Github) is quicker compared to locally. I learnt that say, I want to merge `featureX` to `main`. Locally I would fetch any changes with `git fetch`. Secondly, checkout into `featureX`. I then merge `main` into `featureX`, fix any conflicts if there exists any. I checkout into `main` if everything works out fine. I finally, merge `featureX` into `main`, using `git merge --no-ff featureX` and push to Github. What is the use of `--no-ff`?
