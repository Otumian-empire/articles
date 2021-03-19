# Github Personal Access Token and SSH

Basic authentication is the use of `username` and `password` for authentication. For sometime Github will accept [Basic authentication][basic-auth], the use of `username` and `password`, to access repositories on Github - to clone, push and pull. The Basic authentication will be deprecated very soon this year, [2021][deprecation-url].

Github also allows:

- Username and password with two-factor authentication
- Personal access token (PAT)
- SSH key

## Create the PAT

The PAT can only be used over HTTPS Git operations

- On Github, signup if you don't have an account or login if you already do have one
- At the top right corner, click on your `avatar` and click on `Settings` from the drop-down
- On the left side of your `Setting Profile` page, click on `Developer settings`
- Click on `Personal access token` on the next page
- At the right, click on `Generate token`
- Give the token a name or description and check some privileges you want to give to the token
- Click `Generate token`, a green button at the bottom of the page
- Copy the token and save it somewhere safely (It will still be there when you check it)
- If the token is forgotten or you could not save it, regenerate it.

## Add token to git

vscode is my go-to text editor for my all-round development. Entering the `username` and `token` every time is a nuisance. We would add the `token` globally to git. For a specific application, we can add the token locally. The `token` would be used as the password.

- `git config --global credential.helper store`
- Now clone, push or pull with `username` and copied `token` instead of the `password`

## SSH

- For the sake of testing, let's create a dummy repo on Github. Choose the default settings. (Do not close the page or the browser)
- I am on ubuntu so I will install ssh on ubuntu.
- Update and install `openssh-server`: `sudo apt update` then `sudo apt install openssh-server`
- `sudo systemctl status ssh` to check the `ssh` status then hit `q` to get back to the terminal
- `sudo ufw allow ssh`, will open the `ssh` port. This enables us to connect to our Ubuntu system via SSH from any remote machine.
- `sudo systemctl disable --now ssh` to disable `ssh` and `sudo systemctl enable --now ssh` to enable `ssh`
- Generate `ssh` key, `ssh-keygen -t ed25519 -C "your_email@example.com"`.
- Hit enter to use the default settings for the file name/path to save your key
- Enter and hit enter for the passphrase and reenter the passphrase and hit enter again
- Start the `ssh-agent` in the background to add add key to `ssh-client`: `eval "$(ssh-agent -s)"`
- `ssh-add ~/.ssh/id_ed25519` then enter the passphrase used initially to add key to client
- We can now add the ssh public key to Github. We can cat the public key then copy it or open the public key in a text editor and then copy it.
- `gedit ~/.ssh/id_ed25519.pub` will open the public key in gedit. Copy it.
- On Github just as we did for the toke, go to the top right corner of the page and click on the avatar
- Click on `Settings` on the drop-down
- Click on `SSH and GPG keys`
- Click `New SSH key` or `Add SSH key`.
- add a `title` and then paste the `public key` from the text editor into the `key` field
- Then click on `add SSH Key` and we are done adding ssh key to Github
- The dummy repo we created earlier would have a URL, `https://github.com/username/dummyrepo.git` if we were to use HTTPS but for the SSH, `git@github.com:username/dummyrepo.git`
- Let's clone the project from Github using SSH, `git clone git@github.com:username/dummyrepo.git`
- `cd dummyrepo` and then `echo "# dummyrepo" >> README.md`
- `git add README.md` and `git commit -m "README.md"` to add and commit the `README.md`
- `git push origin main` to push the committed code.

## Switch from HTTPS to SSH URL

Say you have the repo already using HTTPS then you have to change the URL on your local server.

- HTTPS url: `https://github.com/username/dummyrepo.git`
- SSH url: `git@github.com:username/dummyrepo.git`
- check the git url, `git remote -v` which will display

  - `origin https://github.com/username/dummyrepo.git (fetch)`
  - `origin https://github.com/username/dummyrepo.git (push)`

- to change from HTTPS to SSH, `git remote set-url it@github.com:username/dummyrepo.git`
- check the git url verify the changes, `git remote -v`
  - `origin git@github.com:username/dummyrepo.git (fetch)`
  - `origin git@github.com:username/dummyrepo.git (push)`

## Resources

- [Github Basic authentication deprecation][deprecation-url]
- [Authenticating with Github][authenticating-to-github]
- [Enable SSH on Ubuntu][enable-ssh-on-ubuntu]
- [Open-SSH][service-openssh]
- [Generating SSH Keys][ssh-keygen]
- [Awesome git tutorial][learn-git]
- [What is Basic Authentication][what-is-basic-auth]
- [What is Token Authentication][what-is-token-auth]
- [dark image][github-dark]
#

[deprecation-url]: https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api/
[authenticating-to-github]: https://docs.github.com/en/github/authenticating-to-github/about-authentication-to-github
[enable-ssh-on-ubuntu]: https://linuxize.com/post/how-to-enable-ssh-on-ubuntu-20-04/
[service-openssh]: https://ubuntu.com/server/docs/service-openssh
[ssh-keygen]: https://www.ssh.com/ssh/keygen/
[learn-git]: https://dev.to/unseenwizzard/learn-git-concepts-not-commands-4gjc
[basic-auth]: https://en.wikipedia.org/wiki/Basic_access_authentication
[what-is-basic-auth]: https://www.ibm.com/support/knowledgecenter/en/SSGMCP_5.1.0/com.ibm.cics.ts.internet.doc/topics/dfhtl2a.html
[what-is-token-auth]: https://www.okta.com/identity-101/what-is-token-based-authentication/
[github-dark]:https://img.helpnetsecurity.com/wp-content/uploads/2016/11/09105745/github-dark.jpg