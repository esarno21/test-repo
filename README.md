# Coding Project Setup / Notes

###Creating dependencies install file
```bash
pip freeze > requirements.txt
```

# Git Workflow Cheat Sheet

## 🆕 Creating a New Branch
```bash
git switch -c new_branch_name
```

## ✅ Committing Changes
### Stage Files:
```bash
git add .
```
### Commit:
```bash
git commit -m "Message"
```

## 🔄 Pulling from Remote
```bash
git pull origin main  # Or replace 'main' with your branch name
```

## 🚀 Pushing to Remote
```bash
git push -u origin new_branch_name
```

## 🔀 Merging Branches
```bash
git switch main
git pull origin main
git merge new-branch-name
git push origin main
```

## 🗑️ Deleting a Branch
### Delete Local Branch (After Merge)
#### Safe delete (warns if not fully merged)
```bash
git branch -d branch-name
```
#### Force delete (even if not merged)
```bash
git branch -D branch-name
```

### Delete Remote Branch
```bash
git push origin --delete branch-name
```

## ✅ Verifying Deletion
### Check Local Branches:
```bash
git branch
```
### Check Remote Branches:
```bash
git branch -r
```
