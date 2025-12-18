"""Fetch workflow runs and logs for a given branch/PR and print details.

If logs are not accessible without authentication, the script will print check run details and hint to request logs with a GitHub token.
"""
import json
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode

owner = 'JunRoot29'
repo = 'MathCraft'
branch = 'fix/lint-style-centralization'

import os

base_api = f'https://api.github.com/repos/{owner}/{repo}'
# Allow passing a GITHUB_TOKEN to access private logs / archives
token = os.environ.get('GITHUB_TOKEN')
headers = {'User-Agent': 'MathCraft-CI-Inspector', 'Accept': 'application/vnd.github+json'}
if token:
    headers['Authorization'] = f'token {token}'

print('Looking up workflow runs for branch', branch)

# list workflow runs filtered by branch
url = f'{base_api}/actions/runs?branch={branch}&per_page=50'
req = Request(url, headers=headers)
try:
    with urlopen(req) as r:
        data = json.load(r)
except HTTPError as e:
    print('HTTP Error:', e)
    sys.exit(2)

runs = data.get('workflow_runs', [])
if not runs:
    print('No workflow runs found for branch.')
    sys.exit(0)

# Print recent runs and find the one for CI workflow
for run in runs[:10]:
    print(f"Run id={run['id']} name={run['name']} event={run['event']} status={run['status']} conclusion={run.get('conclusion')}")

# Try to find the CI run specifically
ci_runs = [r for r in runs if r.get('name') == 'CI']
if not ci_runs:
    print('No CI workflow runs found for this branch; checking latest run for details...')
    run = runs[0]
else:
    run = ci_runs[0]

run_id = run['id']
print(f"Selected run id={run_id} name={run.get('name')} status={run.get('status')} conclusion={run.get('conclusion')}")

# Attempt to download logs
logs_url = f"{base_api}/actions/runs/{run_id}/logs"
req = Request(logs_url, headers=headers)
try:
    with urlopen(req) as r:
        content_type = r.headers.get('Content-Type')
        print('Fetched logs content-type:', content_type)
        content = r.read()
        if not content:
            print('Logs endpoint returned empty response (may be blocked without auth).')
        else:
            print('Read bytes from response:', len(content))
            fname = f'workflow_{run_id}_logs.zip'
            with open(fname, 'wb') as fh:
                fh.write(content)
            print(f'Saved to {fname}')
        sys.exit(0)
except HTTPError as e:
    print('Could not download logs archive. HTTP status:', e.code, e.reason)
    if token:
        print('Token was provided but download still failed; ensure token has appropriate scopes (repo or actions:read).')
    print('Falling back to checking check-runs for the run commit...')

# Get associated commit SHA
head_sha = run.get('head_sha') or run.get('head_commit', {}).get('id')
if not head_sha:
    print('No head SHA found for run; aborting.')
    sys.exit(0)

# Fetch check-runs for the commit
check_url = f"{base_api}/commits/{head_sha}/check-runs"
req = Request(check_url, headers=headers)
try:
    with urlopen(req) as r:
        checks = json.load(r)
except HTTPError as e:
    print('Could not fetch check-runs:', e)
    sys.exit(2)

print('\nCheck runs for commit', head_sha)
for c in checks.get('check_runs', []):
    print(f"- {c['name']}: status={c['status']} conclusion={c.get('conclusion')} url={c.get('html_url')}")
    # Print a snippet of the output if available
    output = c.get('output') or {}
    text = output.get('text') or output.get('summary') or output.get('title')
    if text:
        print('  output snippet:', (text[:400] + '...') if len(text) > 400 else text)

print('\nIf you need full logs, consider running this script with a GitHub token to access the logs archive:')
print("export GITHUB_TOKEN=ghp_... && python tools/fetch_ci_run_logs.py")
sys.exit(0)