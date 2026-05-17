import subprocess
import base64
import json
import os
import time

REPO = "SuperTony2386/aprocessredesigned.github.io"
API_BASE = f"repos/{REPO}/contents"

def get_file_sha(path):
    """Get the current SHA of a file on GitHub (needed for updates)."""
    result = subprocess.run(
        ["gh", "api", f"{API_BASE}/{path}", "--jq", ".sha"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip()
    return None

def upload_file(local_path, remote_path, commit_msg):
    """Upload a file to GitHub, creating or updating as needed."""
    with open(local_path, 'rb') as f:
        content_bytes = f.read()
    
    content_b64 = base64.b64encode(content_bytes).decode('utf-8')
    
    sha = get_file_sha(remote_path)
    
    payload = {
        "message": commit_msg,
        "content": content_b64,
    }
    if sha:
        payload["sha"] = sha
    
    # Write payload to temp file to avoid shell escaping issues
    with open('/tmp/github_payload.json', 'w') as f:
        json.dump(payload, f)
    
    result = subprocess.run(
        ["gh", "api", f"{API_BASE}/{remote_path}", "-X", "PUT",
         "--input", "/tmp/github_payload.json"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print(f"  ✓ Uploaded: {remote_path}")
        return True
    else:
        print(f"  ✗ FAILED: {remote_path}")
        print(f"    Error: {result.stderr[:200]}")
        return False

# List all files to upload
files_to_upload = []

# Root files
for f in ['index.html', 'search.html', 'about.html', 'social-posts.html']:
    files_to_upload.append((f, f))

# Articles
for f in sorted(os.listdir('articles')):
    if f.endswith('.html'):
        remote = f"articles/{f}"
        local = f"articles/{f}"
        files_to_upload.append((local, remote))

print(f"Uploading {len(files_to_upload)} files to GitHub...\n")

success_count = 0
fail_count = 0

for i, (local, remote) in enumerate(files_to_upload):
    print(f"[{i+1}/{len(files_to_upload)}] {remote}")
    ok = upload_file(local, remote, f"Fix: consistency updates - {remote}")
    if ok:
        success_count += 1
    else:
        fail_count += 1
    # Small delay to avoid rate limiting
    time.sleep(0.5)

print(f"\nDone! Success: {success_count}, Failed: {fail_count}")
