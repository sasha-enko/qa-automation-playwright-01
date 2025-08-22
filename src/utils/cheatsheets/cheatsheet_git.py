cheatsheet_git_commands = [
      {
        "command": "git status",
        "description": "Shows the current state of the working directory and staging area.",
        "scenario": "Use it frequently to see which files are modified, staged, or untracked."
      },
      {
        "command": "git diff",
        "description": "Shows unstaged changes in the working directory.",
        "scenario": "Check what you changed before staging."
      },
      {
        "command": "git diff --staged",
        "description": "Shows changes staged for the next commit.",
        "scenario": "Review what you are about to commit."
      },
      {
        "command": "git add -p",
        "description": "Interactively choose chunks of changes to stage.",
        "scenario": "Clean commits by staging only specific parts of a file."
      },
      {
        "command": "git restore <file>",
        "description": "Restores file content from the last commit (HEAD).",
        "scenario": "Discard changes in working directory for specific files."
      },
      {
        "command": "git restore --staged <file>",
        "description": "Unstages a file without modifying the working directory.",
        "scenario": "If you accidentally staged a file."
      },
      {
        "command": "git log --oneline --graph --all",
        "description": "Compact view of commit history with branch graph.",
        "scenario": "Quick overview of project history."
      },
      {
        "command": "git show <commit>",
        "description": "Shows changes introduced by a specific commit.",
        "scenario": "Inspect details of one commit."
      },
      {
        "command": "git reflog",
        "description": "Shows the history of HEAD moves.",
        "scenario": "Recover lost commits or branches."
      },
      {
        "command": "git rebase -i HEAD~3",
        "description": "Interactive rebase of the last 3 commits.",
        "scenario": "Squash, reword, or reorder commits before pushing."
      },
      {
        "command": "git cherry-pick <commit>",
        "description": "Applies the changes from a specific commit to the current branch.",
        "scenario": "Bring one fix from another branch without merging everything."
      },
      {
        "command": "git revert <commit>",
        "description": "Creates a new commit that undoes the changes of a given commit.",
        "scenario": "Safely revert a bad commit without rewriting history."
      },
      {
        "command": "git commit --amend",
        "description": "Amends the last commit (message or staged files).",
        "scenario": "Fix the most recent commit before pushing."
      },
      {
        "command": "git reset --soft HEAD~1",
        "description": "Undo last commit but keep changes staged.",
        "scenario": "Change the last commit but reuse its content."
      },
      {
        "command": "git reset --mixed HEAD~1",
        "description": "Undo last commit and move changes back to working directory.",
        "scenario": "Rework the last commit from scratch."
      },
      {
        "command": "git reset --hard HEAD~1",
        "description": "Undo last commit and discard all changes.",
        "scenario": "Remove a bad commit completely (dangerous!)."
      },
      {
        "command": "git stash",
        "description": "Temporarily saves changes in a stack.",
        "scenario": "Switch branches without committing work-in-progress."
      },
      {
        "command": "git stash pop",
        "description": "Restores stashed changes and removes them from stash list.",
        "scenario": "Continue working on your previous changes."
      },
      {
        "command": "git stash branch <branch>",
        "description": "Creates a new branch and applies stash to it.",
        "scenario": "Move stashed work to a dedicated branch."
      },
      {
      "command": "git stash drop [stash@{n}]",
      "description": "Deletes a specific stash from the stash list.",
      "scenario": "Use to remove a stash you no longer need after applying or reviewing it."
      },
      {
      "command": "git stash clear",
      "description": "Removes all stashes from the stash list.",
      "scenario": "Use to completely clean the stash stack when all saved work is no longer needed."
      },
      {
        "command": "git branch",
        "description": "Lists all local branches.",
        "scenario": "Quickly see which branches exist and which one is currently checked out."
      },
      {
        "command": "git branch -a",
        "description": "Lists all local and remote-tracking branches.",
        "scenario": "Check all branches including those from remote repositories."
      },
      {
        "command": "git branch <branch-name>",
        "description": "Creates a new branch locally without switching to it.",
        "scenario": "Prepare a new branch for later use."
      },
      {
        "command": "git checkout -b <branch-name>",
        "description": "Creates a new branch and immediately switches to it.",
        "scenario": "Start working on a new feature quickly."
      },
      {
        "command": "git branch -m <old-name> <new-name>",
        "description": "Renames a local branch.",
        "scenario": "Correct or update a branch name."
      },
      {
        "command": "git branch -d <branch-name>",
        "description": "Deletes a local branch if it has been merged.",
        "scenario": "Clean up branches that are no longer needed."
      },
      {
        "command": "git branch -D <branch-name>",
        "description": "Forcibly deletes a local branch even if it has unmerged changes.",
        "scenario": "Remove unwanted branches quickly, losing unmerged work."
      },
      {
        "command": "git branch -vv",
        "description": "Shows last commit and upstream info for each branch.",
        "scenario": "Check branch tracking status and latest commits."
      },
      {
        "command": "git branch --merged",
        "description": "Lists branches already merged into the current branch.",
        "scenario": "Find branches that can be safely deleted."
      },
      {
        "command": "git branch --no-merged",
        "description": "Lists branches not yet merged into the current branch.",
        "scenario": "Identify branches with work that still needs to be integrated."
      },
      {
        "command": "git branch --unset-upstream",
        "description": "Removes upstream tracking information.",
        "scenario": "Unlink a branch from its remote counterpart."
      },
      {
        "command": "git branch -u origin/<branch>",
        "description": "Sets upstream (tracking) branch.",
        "scenario": "Enable simple 'git pull' and 'git push' without arguments."
      },
      {
        "command": "git push origin <branch>",
        "description": "Push a local branch to remote.",
        "scenario": "Create a new remote branch."
      },
      {
        "command": "git push -u origin <branch>",
        "description": "Push branch and set upstream tracking.",
        "scenario": "After creating a new branch, link it to remote."
      },
      {
        "command": "git push origin --delete <branch>",
        "description": "Deletes a branch from remote repository.",
        "scenario": "Clean up obsolete branches."
      },
      {
        "command": "git remote -v",
        "description": "Lists remote repositories and their URLs.",
        "scenario": "Check configured remotes."
      },
      {
        "command": "git merge --no-ff <branch>",
        "description": "Merges with a merge commit even if fast-forward is possible.",
        "scenario": "Keep a clear history of branch merges."
      },
      {
      "command": "git blame <file>",
      "description": "Shows who last modified each line of a file and in which commit.",
      "scenario": "Use to identify the author of specific lines or to debug when a change was introduced."
      },
      {
      "command": "git config --global alias.st status",
      "description": "Creates 'git st' as a shortcut for 'git status'.",
      "scenario": "Quickly check the state of the working directory and staging area."
      },
      {
      "command": "git config --global alias.co checkout",
      "description": "Creates 'git co' as a shortcut for 'git checkout'.",
      "scenario": "Switch branches faster."
      },
      {
      "command": "git config --global alias.br branch",
      "description": "Creates 'git br' as a shortcut for 'git branch'.",
      "scenario": "List, create, or delete branches quickly."
      },
      {
      "command": "git config --global alias.lg \"log --oneline --graph --all\"",
      "description": "Creates 'git lg' as a shortcut for a compact log with graph.",
      "scenario": "View the commit history with branch structure at a glance."
      },
      {
      "command": "git config --global alias.last \"log -1 HEAD\"",
      "description": "Shows the most recent commit with 'git last'.",
      "scenario": "Quickly inspect the last commit made."
      },
      {
      "command": "git config --global alias.unstage \"reset HEAD --\"",
      "description": "Creates 'git unstage' to remove files from staging area.",
      "scenario": "Undo 'git add' for files you staged by mistake."
      },
      {
      "command": "git config --global alias.cm \"commit -m\"",
      "description": "Creates 'git cm' to commit with a message in one step.",
      "scenario": "Faster commit command for small changes."
      }
]


cheatsheet_git_workflows = [
      {
        "name": "Feature development",
        "steps": [
          "git checkout -b feature-login",
          "make changes, git add, git commit",
          "git push -u origin feature-login",
          "open Pull Request on GitHub/GitLab"
        ]
      },
      {
        "name": "Hotfix",
        "steps": [
          "git checkout main",
          "git pull",
          "git checkout -b hotfix-123",
          "fix bug, git commit",
          "git push -u origin hotfix-123"
        ]
      },
      {
        "name": "Sync with remote cleanly",
        "steps": [
          "git checkout main",
          "git fetch origin",
          "git rebase origin/main"
        ]
      },
      {
        "name": "Clean history before push",
        "steps": [
          "git rebase -i HEAD~5",
          "squash or reword commits",
          "git push"
        ]
      },
      {
        "name": "Merge feature into main (with merge commit)",
        "steps": [
          "git checkout main",
          "git pull",
          "git merge --no-ff feature-branch",
          "git push origin main"
        ]
      },
      {
        "name": "Merge feature into main (rebase + fast-forward)",
        "steps": [
          "git checkout feature-branch",
          "git rebase main",
          "git checkout main",
          "git merge feature-branch",
          "git push origin main"
        ]
      },
      {
        "name": "Squash commits before merge",
        "steps": [
          "git checkout feature-branch",
          "git rebase -i HEAD~N (choose squash)",
          "git checkout main",
          "git merge feature-branch",
          "git push origin main"
        ]
      }
]
