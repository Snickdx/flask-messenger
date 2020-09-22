[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/uwidcit/info2602ps.git) 

[![Run on Repl.it](https://repl.it/badge/github/uwidcit/info2602ps)](https://repl.it/github/uwidcit/info2602ps)

# Before you start
Create a heroku account by following this [link](https://signup.heroku.com/login)
You will also need a github account.

# Creating & Linking your own github repository
Git is used to perform source control. It helps teams manage code bases and merge together their contributions.
Github is a free Git server for developers to host their git repositories.

When the project is launched on gitpod (by clicking the gitpod button above), it will already be linked to this starter github repository. To link it to a new repository you need to first run the following command.

```
rm - rf .git
```
Now you can initialize a new git workspace by executing the following.


```
git init
```

Next, create your respository on github by following this [link](https://github.com/new). Give it a name and click on the green "Create Repository" button below.
The next page would give you instructions on how to link the repository to an existing workspace.

Copy the command which looks like.

```
git remote add origin https://github.com/<username>/<reponame>.git
```
Paste and run the command in gitpod.

Your workspace should now be linked to your repository

# Pushing changes to Git
Now the workspace is linked with a git repository it will track all the changes you make to its files.
Run the following command to select which files will be **staged** (tracked for changes)

```
git stage *
```

This will stage all files in the workspace.
Then You prepare the changes to be sent to the repository by making a **commit**. You must supply a custom commit message when making commits.
Run the following command

```
git commit -m "first commit"
```

Finally you can send your changes to the repository by performing a **push**.

```
git push -u origin master
```
At this point you want to **delete** this workspace from the [gitpod dashboard](https://gitpod.io/workspaces/) so that you can create a new workspace from your new repository. 

To create a new workspace go to your repository on github and prepend "https://gitpod.io/#" to the address in the url bar then navigate to that address.

![Editing Address bar](/img/url.png)

Your new workspace should be created on gipod. This will allow you to use the version control UI in gitpod to push changes to github.

# Heroku Setup
Go to the [heroku dashboard](https://dashboard.heroku.com/apps) to create a new app.

![New App](/img/hero-1.png)

From there navigate to the deploy tab of the app.

![deploy](/img/deploy.png)

Then scroll down to deployment method and click github.

![New App](/img/hero-2.png)

Select your newly created repository and click connect.

![New App](/img/hero-3.png)

You can then manually deploy your repository by scrolling down and clicking deploy branch.

![New App](/img/hero-5.png)

You app should then be deployed

![New App](/img/hero-6.png)

From that point on any code pushed to the git repository will be automatically deployed to heroku.