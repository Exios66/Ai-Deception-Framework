import os
import re
import sqlite3
from datetime import datetime
from subprocess import check_output, CalledProcessError

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set the path to CHANGELOG.md relative to the script location
changelog_path = os.path.join(script_dir, 'CHANGELOG.md')

def get_current_version():
    try:
        with open(changelog_path, 'r') as f:
            content = f.read()
            match = re.search(r'## \[(\d+\.\d+\.\d+)\]', content)
            if match:
                return match.group(1)
    except FileNotFoundError:
        print(f"CHANGELOG.md not found at {changelog_path}. Creating a new one.")
        return "0.0.0"
    return "0.0.0"

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor}.{patch + 1}"

def get_commit_messages():
    try:
        current_version = get_current_version()
        print(f"Current version from changelog: {current_version}")

        all_tags = check_output(['git', 'tag']).decode().split()
        print(f"All tags: {all_tags}")

        if all_tags:
            if current_version in all_tags:
                print(f"Found tag for version {current_version}")
                last_version_hash = check_output(['git', 'rev-list', '-n', '1', current_version]).decode().strip()
            else:
                print(f"No tag found for version {current_version}. Using latest tag.")
                latest_tag = all_tags[-1]
                last_version_hash = check_output(['git', 'rev-list', '-n', '1', latest_tag]).decode().strip()
            commit_messages = check_output(['git', 'log', f'{last_version_hash}..HEAD', '--pretty=format:%s']).decode().split('\n')
        else:
            print("No tags found. Getting all commit messages.")
            commit_messages = check_output(['git', 'log', '--pretty=format:%s']).decode().split('\n')

        print(f"Number of commit messages: {len(commit_messages)}")
        return commit_messages
    except CalledProcessError as e:
        print(f"Error getting commit messages: {e}")
        return ["Error retrieving commit messages"]

def update_changelog(new_version, commit_messages):
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"""## [{new_version}] - {today}

### Added
{format_commit_messages(commit_messages)}

"""
    try:
        with open(changelog_path, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(new_entry + content)
    except FileNotFoundError:
        with open(changelog_path, 'w') as f:
            f.write(new_entry)

def format_commit_messages(messages):
    return "\n".join(f"- {msg}" for msg in messages if msg)

def main():
    current_version = get_current_version()
    print(f"Current version: {current_version}")
    new_version = increment_version(current_version)
    print(f"New version: {new_version}")
    commit_messages = get_commit_messages()
    print(f"Commit messages: {commit_messages[:5]}...")  # Print first 5 messages
    update_changelog(new_version, commit_messages)
    print(f"CHANGELOG.md updated with version {new_version}")

if __name__ == "__main__":
    main()