#!/usr/bin/env python3
"""
SSH Push Wrapper - Catches SSH auth errors and auto-fixes
Usage: python3 ssh_push.py <git_dir> [remote] [branch]
"""

import subprocess
import sys
import os
import re

SSH_FIX_SCRIPT = os.path.expanduser("~/Documents/Troubleshooting/fix_ssh_agent.sh")
SSH_CHECK_SCRIPT = os.path.expanduser("~/Documents/Troubleshooting/check_and_fix_ssh.sh")
MAX_RETRIES = 2


def run_cmd(cmd, cwd=None, check=True):
    """Run shell command and return result."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, capture_output=True, text=True
    )
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, cmd, result.stdout, result.stderr)
    return result


def is_ssh_error(stderr):
    """Check if error is SSH auth related."""
    patterns = [
        "Permission denied",
        "publickey",
        "Could not read from remote repository",
        "No such device or address",
    ]
    return any(p in stderr for p in patterns)


def fix_ssh():
    """Run the SSH check/fix script."""
    print("🔧 SSH auth failed. Running check and fix script...")
    try:
        result = run_cmd(f"bash {SSH_CHECK_SCRIPT}", check=False)
        print(result.stdout)
        if result.stderr:
            print(f"⚠️ {result.stderr}", file=sys.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Failed to run fix script: {e}", file=sys.stderr)
        return False


def git_push(git_dir, remote="origin", branch="main"):
    """Try to git push with auto-fix on SSH error."""
    cwd = os.path.expanduser(git_dir)
    
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"🚀 Push attempt {attempt}/{MAX_RETRIES}...")
        
        try:
            # First check if there are commits to push
            result = run_cmd(f"git log {remote}/{branch}..{branch} --oneline", cwd=cwd, check=False)
            commits_ahead = result.stdout.strip()
            
            if not commits_ahead:
                print("✅ Already up to date.")
                return True
            
            # Try to push
            result = run_cmd(f"git push {remote} {branch}", cwd=cwd, check=False)
            
            if result.returncode == 0:
                print(f"✅ Push successful!")
                return True
            
            # Check if SSH error
            if is_ssh_error(result.stderr + result.stdout):
                if attempt < MAX_RETRIES and fix_ssh():
                    continue  # Retry after fix
                else:
                    print("❌ SSH fix failed or max retries reached.", file=sys.stderr)
                    print(f"Error: {result.stderr}", file=sys.stderr)
                    return False
            else:
                print(f"❌ Push failed: {result.stderr}", file=sys.stderr)
                return False
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {e}", file=sys.stderr)
            if attempt < MAX_RETRIES:
                continue
            return False
    
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ssh_push.py <git_dir> [remote] [branch]")
        print("Example: python3 ssh_push.py ~/Desktop/gitStuff/openClaw_Environment")
        sys.exit(1)
    
    git_dir = os.path.expanduser(sys.argv[1])
    remote = sys.argv[2] if len(sys.argv) > 2 else "origin"
    branch = sys.argv[3] if len(sys.argv) > 3 else "main"
    
    if not os.path.isdir(os.path.join(git_dir, ".git")):
        print(f"❌ Not a git repo: {git_dir}", file=sys.stderr)
        sys.exit(1)
    
    success = git_push(git_dir, remote, branch)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
