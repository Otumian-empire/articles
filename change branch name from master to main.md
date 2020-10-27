# Change branch name from master to main

By google-ing, we'd find a  simple command as `git branch -m master main` which should rename the `master` branch to `main`.

What if it was not successful and you had,

```
error: refname refs/heads/master not found
fatal: Branch rename failed
```

Well, in my case, I  create a new project then I initialized git. I then remembered that by default, on Github, the default branch is `main` and not `master` anymore.

You can change the name from `master` to `main` in few steps, locally before you even make a commit.

1. Navigate to the directory where your project sits.
2. In it, show hidden file since by default, `.git` would be hidden.
3. Inside `.git`, there is a file, `HEAD`, open it in a text editor. You'd see, `ref: refs/heads/master`.
4. Simple enough, change, `master` to `main`.

We just renamed the `master` branch as `main`. Verify this merely by entering, `git branch` from the terminal.

