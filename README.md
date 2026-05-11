# 🚀 DevOps Backend: Phase One Runbook

This cheat sheet contains the essential commands for configuring a Fedora Linux workstation, managing Python environments, and executing professional Git/GitHub workflows.

## 🏗️ 1. System Foundation (Fedora & DNF)
*Commands for maintaining the OS and installing core tools.*

```bash
# Update OS and refresh metadata
sudo dnf upgrade --refresh -y

# Check local package database for errors
sudo dnf check

# Install Git and Python package manager
sudo dnf install git python3-pip -y

# Install GitPython (for writing Python scripts that control Git)
sudo dnf install python3-GitPython -y

# Install tldr (simplified, readable manual pages)
sudo dnf install tldr -y
```

## 📦 2. Python Virtual Environment (The Bubble)
*Never install Python packages globally on Linux. Always use an isolated environment.*

```bash
# 1. Create the virtual environment
python3 -m venv .venv

# 2. Activate the environment (Look for (.venv) in your terminal)
source .venv/bin/activate

# 3. Deactivate when finished
deactivate

# Run a Python script (make sure your bubble is active first)
python3 filename.py
```

## 🛡️ 3. Git & SSH Setup (One-Time Configuration)
*Industry-standard secure communication with GitHub.*

```bash
# Set global Git identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Generate SSH Key (Your digital fingerprint)
ssh-keygen -t ed25519 -C "your.email@example.com"

# View your public key to copy to GitHub
cat ~/.ssh/id_ed25519.pub

# Test the secure connection handshake
ssh -T git@github.com
```

## 🐙 4. GitHub CLI (No-Browser Workflow)
*Create and link repositories entirely from the terminal.*

```bash
# Install GitHub CLI
sudo dnf install gh

# Authenticate with GitHub (Select SSH when prompted)
gh auth login

# Create a new repo, link local folder, and push immediately
gh repo create your-project-name --public --source=. --remote=origin --push
```

## 🛰️ 5. Daily Git Workflow
*The commands used every day to save and sync code.*

```bash
# Check the status of your files
git status

# Stage all changed files
git add .

# Save a snapshot with a message
git commit -m "Your descriptive message here"

# Push local changes to the cloud
git push
```

## 🧹 6. Git Cleanup & .gitignore
*How to force Git to forget files it shouldn't be tracking (like `.venv` or `.idea`).*

```bash
# Add common junk folders to your ignore list
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".idea/" >> .gitignore

# The Great Reset: Clear Git's cache without deleting files
git rm -r -f --cached .

# Re-add everything cleanly
git add .
```

## 💻 7. Apps & IDEs
*Installing and running your daily tools.*

```bash
# Install DBeaver (Database tool)
flatpak install flathub io.dbeaver.DBeaverCommunity -y

# Install PyCharm Community
flatpak install flathub com.jetbrains.PyCharm-Community -y

# Run PyCharm silently in the background (prevents terminal log spam)
flatpak run com.jetbrains.PyCharm-Community . > /dev/null 2>&1 &

# Force-kill a stuck PyCharm process
pkill -f pycharm
```

## 🛠️ 8. Linux Daily Drivers & Help
*Navigating the "Engine Room" and finding answers.*

```bash
# File System & Permissions
mkdir -p ~/Path/To/Folder  # Create directory structure
ls -la                     # List all files, including hidden ones
chmod +x script.py         # Make a file executable
df -h                      # Check server disk space

# Searching & History
grep "ERROR" server.log    # Search for text inside a file
history | grep mkdir       # Find a forgotten command in your history

# Getting Help
man <command>              # Official deep-dive manual
apropos "copy files"       # Search for a command by what it does
tldr <command>             # Quick, practical examples of a command
```