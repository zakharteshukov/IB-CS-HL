#!/bin/bash
# Script to publish the repository to GitHub
# 
# Option 1: Create repo manually on GitHub.com, then run:
#   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
#   git branch -M main
#   git push -u origin main
#
# Option 2: If you have GitHub CLI installed, run:
#   gh repo create YOUR_REPO_NAME --public --source=. --remote=origin --push

REPO_NAME="IB-CS-HL"
GITHUB_USER="zakharteshukov"

echo "To publish this repository to GitHub:"
echo ""
echo "1. Create a new repository on GitHub.com named: $REPO_NAME"
echo "   (or choose your own name)"
echo ""
echo "2. Then run these commands:"
echo ""
echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Or if you have GitHub CLI (gh) installed:"
echo "   gh repo create $REPO_NAME --public --source=. --remote=origin --push"

