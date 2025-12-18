import json
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

owner = 'JunRoot29'
repo = 'MathCraft'
job_id = 58408322789

import os

base_api = f'https://api.github.com/repos/{owner}/{repo}'
# Allow passing a GITHUB_TOKEN to access extended job logs
token = os.environ.get('GITHUB_TOKEN')
headers = {'User-Agent': 'MathCraft-Job-Inspector', 'Accept': 'application/vnd.github+json'}
if token:
    headers['Authorization'] = f'token {token}'

url = f'{base_api}/actions/jobs/{job_id}'
req = Request(url, headers=headers)
try:
    with urlopen(req) as r:
        data = json.load(r)
except HTTPError as e:
    print('HTTP Error:', e)
    sys.exit(2)

# Print job status and steps
print('Job id:', data.get('id'))
print('Status:', data.get('status'), 'Conclusion:', data.get('conclusion'))
print('Name:', data.get('name'))
print('Run id:', data.get('run_id'))

steps = data.get('steps', [])
print('\nSteps:')
for s in steps:
    print('-', s.get('name'), 'status=', s.get('status'), 'conclusion=', s.get('conclusion'))

# Try to fetch annotations or logs_url
print('\nLog URL (may require auth):', data.get('logs_url'))
print('URL to web job page:', data.get('html_url'))

# If 'steps' include 'conclusion' failed, print details
for s in steps:
    if s.get('conclusion') and s.get('conclusion') != 'success':
        print('\nFailed step:', s.get('name'))
        output = s.get('output', {})
        if output:
            print('output summary:', output.get('summary'))
            print('output text snippet:', (output.get('text') or '')[:800])

print('\nIf more logs needed, run with a GITHUB_TOKEN env var to download logs archive or fetch job logs via the API with authentication.')